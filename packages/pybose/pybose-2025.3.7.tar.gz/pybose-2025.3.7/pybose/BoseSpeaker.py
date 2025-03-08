"""
Bose Speaker control using its Websocket (like the BOSE app)

In order to control the device locally, you need to obtain the control token and device ID.
The control token needs to be aquired from the online BOSE API. The script "BoseAuth.py" can be used to obtain the control token using the email and password of the BOSE account.
The device ID can be obtained by discovering the device on the local network using the script "BoseDiscovery.py".

The token is only valid for a certain amount of time AND does not renew automatically.
So you may need to refetch the token from time to time.
"""

import json
import asyncio
import logging
from ssl import SSLContext, CERT_NONE
import websockets
from threading import Event
from .BoseResponse import (
    ActiveGroup,
    AudioVolume,
    ContentNowPlaying,
    SystemInfo,
    SystemPowerControl,
    Sources,
    Audio,
    Accessories,
    Battery,
    Preset,
    AudioMode,
    DualMonoSettings,
    RebroadcastLatencyMode,
)
import sys

# These are the default resources that are subscribed to when connecting to the speaker by the BOSE app
DEFAULT_SUBSCRIBE_RESOURCES = [
    "/bluetooth/sink/list",
    "/system/power/control",
    "/audio/avSync",
    "/bluetooth/source/list",
    "/audio/bass",
    "/device/assumed/TVs",
    "/network/wifi/siteScan",
    "/system/update/start",
    "/system/update/status",
    "/bluetooth/sink/macAddr",
    "/content/nowPlaying/rating",
    "/bluetooth/source/stopScan",
    "/system/setup",
    "/homekit/info",
    "/bluetooth/source/pairStatus",
    "/device/configuredDevices",
    "/bluetooth/source/status",
    "/cast/teardown",
    "/bluetooth/sink/status",
    "/cast/setup",
    "/cec",
    "/cloudSync",
    "/system/challenge",
    "/bluetooth/sink/remove",
    "/bluetooth/source/connect",
    "/remote/integration/brandList",
    "/subscription",
    "/network/status",
    "/bluetooth/source/scanResult",
    "/content/playbackRequest",
    "/audio/eqSelect",
    "/audio/height",
    "/content/transportControl",
    "/grouping/activeGroups",
    "/audio/mode",
    "/bluetooth/source/pair",
    "/bluetooth/source/capability",
    "/bluetooth/source/disconnect",
    "/audio/subwooferGain",
    "/voice/setup/start",
    "/audio/center",
    "/network/wifi/status",
    "/content/nowPlaying/repeat",
    "/system/sources",
    "/content/nowPlaying",
    "/system/power/macro",
    "/bluetooth/sink/pairable",
    "/network/wifi/profile",
    "/cast/settings",
    "/audio/zone",
    "/content/nowPlaying/shuffle",
    "/bluetooth/source/capabilitySettings",
    "/remote/integration",
    "/audio/surround",
    "/accessories",
    "/audio/treble",
    "/adaptiq",
    "/accessories/playTones",
    "/system/power/timeouts",
    "/audio/dualMonoSelect",
    "/system/info",
    "/system/sources/status",
    "/audio/rebroadcastLatency/mode",
    "/audio/format",
    "/bluetooth/source/connectionStatus",
    "/system/power/mode/opticalAutoWake",
    "/content/nowPlaying/favorite",
    "/system/productSettings",
    "/bluetooth/sink/connectionStatus",
    "/bluetooth/source/remove",
    "/audio/autoVolume",
    "/system/capabilities",
    "/audio/volume/increment",
    "/bluetooth/sink/connect",
    "/bluetooth/source/volume",
    "/bluetooth/sink/disconnect",
    "/system/reset",
    "/audio/volume/decrement",
    "/audio/volume",
    "/remote/integration/directEntry",
    "/device/configure",
    "/device/setup",
    "/bluetooth/source/scan",
    "/voice/settings",
    "/system/activated",
]


class BoseSpeaker:
    def __init__(self, control_token: str, host: str, device_id=None, version=1):
        self._control_token = control_token
        self._device_id = device_id
        self._host = host
        self._version = version
        self._websocket = None
        self._ssl_context = SSLContext()
        self._ssl_context.verify_mode = CERT_NONE
        self._subprotocol = "eco2"
        self._req_id = 1
        self._url = f"wss://{self._host}:8082/?product=Madrid-iOS:31019F02-F01F-4E73-B495-B96D33AD3664"
        self._responses = []
        self._stop_event = Event()
        self._receiver_task = None
        self._receivers = {}
        self._subscribed_resources = []
        self._message_queue = asyncio.Queue()

    async def connect(self):
        """Connect to the WebSocket and start the receiver task."""
        self._websocket = await websockets.connect(
            self._url, subprotocols=[self._subprotocol], ssl=self._ssl_context
        )
        logging.info("WebSocket connection established.")

        self._stop_event.clear()
        self._receiver_task = asyncio.create_task(self._receiver_loop())
        if len(self._subscribed_resources) > 0:
            logging.debug("Subscribing to resources from previous session.")
            await self.subscribe(self._subscribed_resources)

    async def disconnect(self):
        """Stop the receiver task and close the WebSocket."""
        self._stop_event.set()
        if self._receiver_task:
            await self._receiver_task
        if self._websocket:
            await self._websocket.close()
        logging.info("WebSocket connection closed.")

    def attach_receiver(self, callback) -> int:
        """Attach to receiver."""
        id = max(self._receivers.keys(), default=0) + 1
        self._receivers[id] = callback
        return id

    def detach_receiver(self, id):
        """Detach from receiver."""
        self.receivers.pop(id, None)

    async def _request(
        self,
        resource,
        method,
        body={},
        withHeaders=False,
        waitForResponse=True,
        version=None,
    ) -> dict:
        """Send a request and wait for the matching response."""
        token = self._control_token
        req_id = self._req_id
        self._req_id += 1

        if version is None:
            version = self._version

        message = {
            "body": body,
            "header": {
                "token": token,
                "version": version,
                "reqID": req_id,
                "resource": resource,
                "device": self._device_id,
                "msgtype": "REQUEST",
                "method": method,
            },
        }

        if self._device_id is None:
            await self._message_queue.put(message)
            logging.debug(
                f"Waiting for deviceID. Queued message: {json.dumps(message, indent=4)}"
            )
        else:
            if self._websocket is None or self._websocket.close_code is not None:
                logging.warning(
                    "WebSocket connection is closed. Reconnecting before sending message."
                )
                await self.connect()
            await self._websocket.send(json.dumps(message))
            logging.debug(f"Sent message: {json.dumps(message, indent=4)}")

        # Wait for response with matching reqID
        if not waitForResponse:
            return

        # TODO: Refactor from polling to event-driven
        while True:
            for response in self._responses:
                if response["header"]["reqID"] == req_id:
                    self._responses.remove(response)
                    if (
                        "status" in response["header"]
                        and response["header"]["status"] != 200
                    ):
                        raise Exception(
                            f"Request failed with status {response['header']['status']}",
                            response["error"]["code"]
                            if response["header"]["status"] == 500
                            else response["header"]["status"],
                            response["error"]["message"]
                            if response["header"]["status"] == 500
                            else None,
                        )
                    if not withHeaders:
                        return response["body"]
                    return response
            await asyncio.sleep(0.1)

    async def _receiver_loop(self):
        """Async function to receive and process messages."""
        try:
            while not self._stop_event.is_set():
                message = await self._websocket.recv()
                logging.debug(f"Received message: {message}")
                parsed_message = json.loads(message)

                if (
                    "header" in parsed_message
                    and "device" in parsed_message["header"]
                    and self._device_id is None
                ):
                    self._device_id = parsed_message["header"]["device"]
                    while not self._message_queue.empty():
                        message = await self._message_queue.get()
                        message["header"]["device"] = self._device_id
                        await self._websocket.send(json.dumps(message))
                        logging.debug(
                            f"Sent queued message: {json.dumps(message, indent=4)}"
                        )

                # Check if the message is a response to a request
                if "header" in parsed_message and "reqID" in parsed_message["header"]:
                    self._responses.append(parsed_message)
                else:
                    # Notify all receivers about the unsolicited message
                    for receiver in self._receivers.values():
                        receiver(parsed_message)

        except websockets.ConnectionClosed:
            logging.warning("WebSocket connection lost. Attempting to reconnect...")
            await self.connect()  # Reconnect if the connection is lost
            return
        except Exception as e:
            if not self._stop_event.is_set():
                logging.error(f"Error in receiver loop: {e}")

    async def get_capabilities(self):
        """Get the capabilities of the device."""
        return await self._request("/system/capabilities", "GET")

    async def get_system_info(self) -> SystemInfo:
        """Get system info."""
        return SystemInfo(await self._request("/system/info", "GET"))

    async def get_audio_volume(self) -> AudioVolume:
        """Get the current audio volume."""
        return AudioVolume(await self._request("/audio/volume", "GET"))

    async def set_audio_volume(self, volume) -> AudioVolume:
        """Set the audio volume."""
        body = {"value": volume}
        return AudioVolume(await self._request("/audio/volume", "PUT", body))

    async def get_now_playing(self) -> ContentNowPlaying:
        """Get the current playing content."""
        return ContentNowPlaying(await self._request("/content/nowPlaying", "GET"))

    async def get_bluetooth_status(self):
        """Get the Bluetooth status."""
        return await self._request("/bluetooth/source/status", "GET")

    async def get_power_state(self) -> SystemPowerControl:
        """Get the power state of the device."""
        return await self._request("/system/power/control", "GET")

    async def set_power_state(self, state: bool) -> None:
        """Set the power state of the device."""
        body = {"power": "ON" if state else "OFF"}
        await self._request("/system/power/control", "POST", body)

    async def _control_transport(self, control: str) -> ContentNowPlaying:
        """Control the transport."""
        body = {"state": control}
        return ContentNowPlaying(
            await self._request("/content/transportControl", "PUT", body)
        )

    async def pause(self) -> ContentNowPlaying:
        """Pause the current content."""
        return await self._control_transport("PAUSE")

    async def play(self) -> ContentNowPlaying:
        """Play the current content."""
        return await self._control_transport("PLAY")

    async def skip_next(self) -> ContentNowPlaying:
        """Skip to the next content."""
        return await self._control_transport("SKIPNEXT")

    async def skip_previous(self) -> ContentNowPlaying:
        """Skip to the previous content."""
        return await self._control_transport("SKIPPREVIOUS")

    async def seek(self, position):
        """Seek to position (in seconds)."""
        body = {"position": position, "state": "SEEK"}
        return await self._request("/content/transportControl", "PUT", body)

    async def request_playback_preset(self, preset: Preset, initiator_id: str) -> bool:
        """Request a playback preset."""
        content_item = preset.get("actions")[0].get("payload").get("contentItem")
        return await self._request(
            "/content/playbackRequest",
            "POST",
            {
                "source": content_item.get("source"),
                "initiatorID": initiator_id,
                "sourceAccount": content_item.get("sourceAccount"),
                "preset": {
                    "location": content_item.get("location"),
                    "name": content_item.get("name"),
                    "containerArt": content_item.get("containerArt"),
                    "presetable": content_item.get("presetable"),
                    "type": content_item.get("type"),
                },
            },
        )

    def get_device_id(self) -> str | None:
        """Get the device ID."""
        return self._device_id

    async def subscribe(self, resources: list[str] = DEFAULT_SUBSCRIBE_RESOURCES):
        """Subscribe to resources."""
        body = {
            "notifications": [
                {"resource": resource, "version": 1} for resource in resources
            ]
        }
        self._subscribed_resources = resources
        return await self._request("/subscription", "PUT", body, version=2)

    async def switch_tv_source(self) -> ContentNowPlaying:
        """Switch to TV source."""
        return await self.set_source("PRODUCT", "TV")

    async def set_source(self, source, sourceAccount) -> ContentNowPlaying:
        """Set the source."""
        body = {"source": source, "sourceAccount": sourceAccount}
        return ContentNowPlaying(
            await self._request("/content/playbackRequest", "POST", body)
        )

    async def get_sources(self):
        """Get the sources."""
        return Sources(await self._request("/system/sources", "GET"))

    async def get_audio_setting(self, option) -> Audio:
        """Get the audio setting."""
        # TODO: load from capabilities
        if option not in [
            "bass",
            "treble",
            "center",
            "subwooferGain",
            "height",
            "avSync",
        ]:
            raise Exception(f"Invalid audio setting: {option}")
        return Audio(await self._request("/audio/" + option, "GET"))

    async def set_audio_setting(self, option, value) -> Audio:
        """Get the audio setting."""
        # TODO: load from capabilities
        if option not in [
            "bass",
            "treble",
            "center",
            "subwooferGain",
            "height",
            "avSync",
        ]:
            raise Exception(f"Invalid audio setting: {option}")

        return Audio(
            await self._request("/audio/" + option, "POST", {"value": int(value)})
        )

    async def get_accessories(self) -> Accessories:
        """Get the accessories."""
        return Accessories(await self._request("/accessories", "GET"))

    async def put_accessories(self, subs_enabled=None, rears_enabled=None) -> bool:
        if subs_enabled is None and rears_enabled is None:
            accessories = await self.get_accessories()
            if subs_enabled is None:
                subs_enabled = accessories.enabled.subs
            if rears_enabled is None:
                rears_enabled = accessories.enabled.rears

        body = {"enabled": {"rears": rears_enabled, "subs": subs_enabled}}
        return await self._request("/accessories", "PUT", body)

    async def get_battery_status(self) -> Battery:
        """Get the battery status."""
        return Battery(await self._request("/system/battery", "GET"))

    async def get_audio_mode(self) -> AudioMode:
        """Get the audio mode."""
        return AudioMode(await self._request("/audio/mode", "GET"))

    async def set_audio_mode(self, mode) -> bool:
        """Set the audio mode."""
        result = await self._request("/audio/mode", "POST", {"value": mode})
        if result.get("value") == mode:
            return True
        return False

    async def get_dual_mono_setting(self) -> DualMonoSettings:
        """Get the dual mono setting."""
        return DualMonoSettings(await self._request("/audio/dualMonoSelect", "GET"))

    async def set_dual_mono_setting(self, value) -> bool:
        """Set the dual mono setting."""
        result = await self._request("/audio/dualMonoSelect", "POST", {"value": value})
        if result.get("value") == value:
            return True
        return False

    async def get_rebroadcast_latency_mode(self) -> RebroadcastLatencyMode:
        """Get the rebroadcast latency mode."""
        return await self._request("/audio/rebroadcastLatency/mode", "GET")

    async def set_rebroadcast_latency_mode(self, mode) -> bool:
        """Set the rebroadcast latency mode."""
        result = await self._request(
            "/audio/rebroadcastLatency/mode", "PUT", {"mode": mode}
        )
        if result.get("value") == mode:
            return True
        return False

    async def get_active_groups(self) -> list[ActiveGroup]:
        """Get the active groups."""

        groups = await self._request("/grouping/activeGroups", "GET")

        return [ActiveGroup(group) for group in groups.get("activeGroups", [])]

    async def set_active_group(self, other_product_ids: list[str]) -> bool:
        """Set the active group."""

        body = {"products": [{"productId": self._device_id, "role": "NORMAL"}]}

        # add other product ids to body
        for product_id in other_product_ids:
            body["products"].append({"productId": product_id, "role": "NORMAL"})

        return await self._request("/grouping/activeGroups", "POST", body)

    async def add_to_active_group(
        self, active_group_id: str, other_product_ids: list[str]
    ) -> bool:
        """Add to the active group."""
        body = {
            "addProducts": [
                {"productId": product_id, "role": "NORMAL"}
                for product_id in other_product_ids
            ],
            "activeGroupId": active_group_id,
            "addGroups": [],
            "removeGroups": [],
            "removeProducts": [],
        }
        return await self._request("/grouping/activeGroups", "PUT", body)

    async def remove_from_active_group(
        self, active_group_id: str, other_product_ids: list[str]
    ) -> bool:
        """Remove from the active group."""
        body = {
            "name": "",
            "addProducts": [],
            "activeGroupId": active_group_id,
            "addGroups": [],
            "removeGroups": [],
            "removeProducts": [
                {"productId": product_id, "role": "NORMAL"}
                for product_id in other_product_ids
            ],
        }
        return await self._request("/grouping/activeGroups", "PUT", body)

    async def stop_active_groups(self) -> bool:
        """Remove all active groups."""
        return await self._request("/grouping/activeGroups", "DELETE")


# EXAMPLE USAGE


async def main(control_token, device_id, host):
    bose = BoseSpeaker(control_token=control_token, device_id=device_id, host=host)

    # Attach receiver for unsolicited messages
    bose.attach_receiver(
        lambda data: print(
            f"Received unsolicited message: {json.dumps(data, indent=4)}"
        )
    )

    # Connect to the speaker
    await bose.connect()

    # Get system info
    response = await bose.get_system_info()
    print(response)

    # Get audio volume
    response = await bose.get_audio_volume()
    print(response)

    # Set get currently playing content
    response = await bose.get_now_playing()
    print(response)

    # Safely disconnect from the speaker
    await bose.disconnect()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python {sys.argv[0]} <control_token> <device_id> <host>")
        sys.exit(1)

    control_token = sys.argv[1]
    device_id = sys.argv[2]
    host = sys.argv[3]

    asyncio.run(main(control_token, device_id, host))
