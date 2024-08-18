import asyncio
from websockets import connect
import uuid
import json
from epevermodbus.driver import EpeverChargeController

controller = EpeverChargeController("/dev/ttyUSB0", 1)

async def run(uri):
    async with connect(uri) as websocket:
        message = await websocket.recv()
        print(message)

        login_msg = {
                "requestId": str(uuid.uuid4()),
                "login": { "username": "USERNAME", "password": "PASSWORD" }
        }

        await websocket.send(json.dumps(login_msg))
        print("[epever] login sent")
        message = await websocket.recv()
        print(message)

        beacon_msg = {
            "context": "self",
            "updates": [{ "values": [{"path": "electrical.batteries.1.voltage", "value": controller.get_battery_voltage() }]}]
        }
        await websocket.send(json.dumps(beacon_msg))
        print("[epever] beacon sent:", beacon_msg)
        exit(0)

asyncio.run(run("ws://127.0.0.1:3000/signalk/v1/stream?subscribe=none"))
