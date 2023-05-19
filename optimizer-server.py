
import asyncio
import websockets
from websockets.sync.client import connect


def hello(m):
    with connect("ws://localhost:8001") as websocket:
        websocket.send(m)
        message = websocket.recv()
        print(f"Received: {message}")
        return message


async def handler(websocket):
    while True:
        message = await websocket.recv()
        print(message)
        json_string=hello(message)
        await websocket.send(json_string)


async def main():
    async with websockets.serve(handler, "", 8002):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())