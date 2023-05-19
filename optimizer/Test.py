import websockets
from OptimizerWebSocket import WsClient
ws = WsClient("ws://localhost:8001")

lower_bound_list = [-20, -20]
upper_bound_list = [20, 20]
max_evaluations = 1000

message = {
    "variable": {
        "lower_bound_list": lower_bound_list,
        "upper_bound_list": upper_bound_list
    },
    "max_evaluations": max_evaluations
}

# Convertir el diccionario en una cadena json
import json
json_string = json.dumps({"action": "optimize", "message": message})

# Imprimir la cadena json
try:
    objetives=ws.send_data(json_string)
    print(objetives)
except websockets.ConnectionClosedOK:
    pass