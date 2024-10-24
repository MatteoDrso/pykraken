# pykraken
A repository that provides an easy to use, straight forward connection to the Kraken-Crypto API in python.

## modules
As of right now the API supports 3 sockets. Those are:

### Ticker Data Socket (KrakenL1Socket):
This socket streams ticker data/top of the book data.
Source: https://docs.kraken.com/api/docs/websocket-v2/ticker

### Order Book Price Socket (KrakenL2Socket):
This socket streams the order book, i.e. individual price levels with aggregated order quantities.
Source: https://docs.kraken.com/api/docs/websocket-v2/book

### Order Book Socket (KrakenL3Socket):
This socket adds another level of granularity ot the KrakenL2Socket, i.e. shows orders in the visible book.
Source: https://docs.kraken.com/api/docs/websocket-v2/level3

## Functionality
This module implements the basic functionality of the Kraken API sockets. That includes the maintenance of the order book, the calculation and verification of the checksum enforcing the standards of Kraken, the management of private or public connections and the generation of a private token for that matter. 

### Usage
This package only requires 3 external modules, to install them use:
```shell
pip install -r requirements.txt
```
To use the sockets you need to create a socket like this:
```python
from api.sockets import KrakenL3Socket

l3socket = KrakenL3Socket('BTC/USD', depth=10, checksum_freq=100)
l3socket.connect() 
```
As of right now the sockets only maintain the connection. Any further logic like logging to a csv file or connecting to some front end can be implemented.
To implement logic the `_on_message(ws, str)` callback has to be modified. However, the maintenance logic should remain untouched. 

## Future work
My plans for the future are:
- implement more trading functionalities (placing orders, checking account balance, ...)
- add more possibilities to interact with the socket (automate CSV file logging)
- more logging 
- more documentation
- ...

## LICENSE
This product is provided under the MIT License.
