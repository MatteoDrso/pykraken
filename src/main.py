from api.sockets import (
    KrakenL1Socket,
    KrakenL2Socket,
    KrakenL3Socket
)

#example usage:
l1 = KrakenL3Socket('BTC/USD', depth=100)
l1.connect()