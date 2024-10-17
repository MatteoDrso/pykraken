import websocket
import json
from api.sockets import KrakenL1Socket
import time


l1 = KrakenL1Socket('BTC/USD')

l1.connect()


