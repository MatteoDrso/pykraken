from api.sockets import KrakenL3Socket


l1 = KrakenL3Socket('BTC/USD', depth=10)
l1.connect()