
import asyncio
import websockets
import json

lower_bound_list = [-20, -20]
upper_bound_list = [20, 20]
max_evaluations = 100

body= {
    "variable": {
        "lower_bound_list": lower_bound_list,
        "upper_bound_list": upper_bound_list
    },
    "max_evaluations": max_evaluations
}

# Convertir el diccionario en una cadena json

json_string = json.dumps({"action": "optimize", "message": body})

async def handler(websocket):
    while True:
        message = await websocket.recv()
        print(message)
        await websocket.send(json_string)


async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())