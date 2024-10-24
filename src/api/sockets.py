import api.tickers as tickers
from api.errors import InvalidChecksumError
from api.user import get_token

import websocket
import threading
import json
from zlib import crc32

import warnings

from sortedcontainers import SortedDict



KRAKEN_WS_AUTH_URL = 'wss://ws-auth.kraken.com/v2'
KRAKEN_WS_URL = 'wss://ws.kraken.com/v2'



class KrakenSocket:
    """
    Base class of a Kraken Websocket to connect to the Kraken API.
    """

    def __init__(self, auth: bool = True, debug: bool = False):
        self.auth = auth
        self.debug = debug
        self.ws = None


    def connect(self):
        """
        Connect the websocket to the Kraken API.
        """

        thread = threading.Thread(target=self._create_websocket)
        thread.start()

        try:
            thread.join()
        except KeyboardInterrupt:
            print("Aborted by user.")
            self.ws.close()


    def _on_message(self, ws: websocket.WebSocket, message):
        """
        **This function provides the main interface to parse the responses from the server.**

        Handle and parse the incoming server response `message`.
        """

        print("########################################")
        print(message)
        print("########################################")


    def _on_error(self, ws: websocket.WebSocket, error):
        """
        Handle and parse an incoming error from the server `error`.
        """

        print("########################################")
        print(error)
        print("########################################")


    def _on_close(self, ws: websocket.WebSocket):
        """
        Handle the closing of the websocket.
        """
        print("Closing the Kraken socket...")


    def _on_open(self, ws: websocket.WebSocket):
        """
        Handle the opening of the websocket.
        """

        print("Opening the Kraken socket...")

    
    def _create_websocket(self):
        """
        Create websocket instance.
        """
        
        if self.auth:
            url = KRAKEN_WS_AUTH_URL
        else:
            url = KRAKEN_WS_URL

        self.ws = websocket.WebSocketApp(url, 
                                         on_open = self._on_open,
                                         on_message = self._on_message,
                                         on_error = self._on_error,
                                         on_close = self._on_close)

        websocket._logging.enableTrace(traceable=self.debug)

        self.ws.run_forever()


    def _ensure_pair_validity(self, pair: str, on_invalid: str = 'drop') -> list[str]:
        """
        Ensure the validity of the passed pair list `pairs` so that they
        coincide with the formatting of Kraken.
        """
        
        if type(pair) != str:
            #TODO: support multiple pairs.
            raise TypeError(f"The pair passed have to be a single string, not {type(pair)}.",
                             "If you want to have multiple data streams, please use multiple sockets.")

        if pair in tickers.KRAKEN_PAIRS:
            return [pair]
        else:
            match on_invalid:
                case 'drop':
                    warnings.warn(f"{pair} not in api.tickers, you might have to update that list.")
                case 'raise':
                    raise KeyError(f"{pair} not in api.tickers, you might have to update that list.")


    def _json_subcribe_message(self, params: dict, token: str = None) -> str:
        """
        Create json message to subscribe to a Kraken API Socket.
        """
        
        json_message = {'method':'subscribe'}
        json_message['params'] = params

        if token:
            json_message['params']['token'] = token

        return json.dumps(json_message)


    def _format_kraken_str(self, x: float, precision: int) -> str:
        """
        Format a float `x` with given precision `precision` to Kraken API standards.
        """

        x = f"{x:.{precision}f}"
        x = x.replace('.', '').lstrip('0')

        return x




class KrakenL1Socket(KrakenSocket):
    """
    Kraken Level 1 Websocket to connect to the Kraken API. 
    Streams ticker/top of the book (best bid/ask) market data and recent trade data.

    =====
    Source: https://docs.kraken.com/api/docs/websocket-v2/ticker
    """

    def __init__(self, symbol: str, high_freq: bool = False,
                 on_invalid: str = 'raise', debug: bool = False):

        self.symbol = self._ensure_pair_validity(symbol, on_invalid=on_invalid)
        self.event_trigger = 'trades' if high_freq else 'bbo'

        super().__init__(auth=False, debug=debug)

        self.count = 0


    def _on_close(self, ws: websocket.WebSocket, close_status_code: int, close_msg: str):
        """
        Handle the closing of the websocket.
        """

        print("Closing the Kraken L1 socket...")
        print(f"{self.count} ticker messages received and handled.")


    def _on_error(self, ws: websocket.WebSocket, error: str):
        """
        Handle the error of the websocket.
        """
    
        print(f"Received error: {error}")


    def _on_message(self, ws: websocket.WebSocket, message: str): 
        """
        **This function provides the main interface to parse the responses from the server.**

        Handle and parse the incoming server response `message`.
        """

        response = json.loads(message)
        
        if response.get('channel', "") == 'status' or response.get('channel', "") == 'heartbeat':
            pass
        else:
            if self.count == 0: # skip subscription ack.
                pass
            else:
                if (channel := response.get('channel', "")) != 'ticker':
                    warnings.warn(f"expected channel: ticker, got {channel} instead.")
                else:
                    data = response['data'][0]
                    print(
                        f"{self.symbols} ${data['last']}, {data['change']} ({data['change_pct']}%)\n" +
                        f"bid: {data['bid']} ({data['bid_qty']})\n" +
                        f"ask: {data['ask']} ({data['ask_qty']})\n" +
                        f"vwap: {data['vwap']}"
                    )
            self.count += 1

    
    def _on_open(self, ws: websocket.WebSocket):
        """
        Handles the opening of the socket and the sending of the subscription request.
        """

        subscription_params = {
            'channel': 'ticker',
            'symbol': self.symbol,
            'event_trigger': self.event_trigger,
        }

        self.ws.send(self._json_subcribe_message(subscription_params))




class KrakenL2Socket(KrakenSocket):
    """
    Kraken Level 2 Websocket to connect to the Kraken API. 
    Streams the order book, i.e. individual price levels with aggregated order quantities.

    =====
    Source: https://docs.kraken.com/api/docs/websocket-v2/book
    """

    BOOK_DEPTHS = [10, 25, 100, 500, 1000]

    def __init__(self, symbol: str, depth: int = 10,
                 checksum_freq: int = 10, on_invalid: str = 'raise',
                 debug: bool = False):

        self.symbol = self._ensure_pair_validity(symbol, on_invalid=on_invalid)
        
        self.bids = SortedDict()
        self.asks = SortedDict()

        if depth not in KrakenL2Socket.BOOK_DEPTHS:
            raise ValueError(f"The book depth has to be in {KrakenL2Socket.BOOK_DEPTHS}.")
        
        self.depth = depth

        super().__init__(auth=False, debug=debug)

        self.checksum_freq = checksum_freq
        self.count = 0


    def _on_close(self, ws: websocket.WebSocket, close_status_code: int, close_msg: str):
        """
        Handle the closing of the websocket.
        """

        print("Closing the Kraken L2 socket...")
        print(f"{self.count} ticker messages received and handled.")


    def _on_error(self, ws: websocket.WebSocket, error: str):
        """
        Handle the error of the websocket.
        """
        
        print(f"\nReceived error: {error}\n")


    def _on_message(self, ws: websocket.WebSocket, message: str):
        """
        **This function provides the main interface to parse the responses from the server.**

        Handle and parse the incoming server response `message`.
        """

        response = json.loads(message)

        #LOGIC TO MAINTAIN THE ORDER BOOK
        #skip status and hearbeat messages
        if response.get('channel', "") == 'status' or response.get('channel', "") == 'heartbeat':
            pass

        else:
            if self.count == 0: # skip subscription ack.
                pass

            else:
                data = response['data'][0]

                if response['type'] == 'snapshot':
                    self.bids, self.asks = self._create_book_from_snapshot(response)                   
                
                else:
                    bids = data['bids']
                    asks = data['asks']

                    for bid in bids:
                        if bid['qty'] == 0:
                            del self.bids[bid['price']]
                        else:
                            self.bids[bid['price']] = bid['qty'] 
                    
                    for ask in asks:
                        if ask['qty'] == 0:
                            del self.asks[ask['price']]
                        else:
                            self.asks[ask['price']] = ask['qty'] 


                    overflow_asks = len(self.asks) - self.depth
                    overflow_bids = len(self.bids) - self.depth

                    for ask_price in reversed(self.asks):
                        if overflow_asks == 0:
                            break
                        overflow_asks -= 1
                        del self.asks[ask_price]
                 
                    for bid_price in self.bids:
                        if overflow_bids == 0:
                            break
                        overflow_bids -= 1
                        del self.bids[bid_price]


                if self.count % self.checksum_freq == 0:

                    checksum = data['checksum']

                    if not self._verify_checksum(checksum):
                        #TODO: at this point you would probably want to rebuild the book, instead of throwing an Error.
                        raise InvalidChecksumError("The checksum verification failed.") 
                
            self.count += 1

    
    def _on_open(self, ws: websocket.WebSocket):
        """
        Handles the opening of the socket and the sending of the subscription request.
        """

        print("Kraken L2 Socket opened.")

        subscription_params = {
            'channel': 'book',
            'symbol': self.symbol,
            'depth': self.depth,
        }

        self.ws.send(self._json_subcribe_message(subscription_params))          


    def _create_book_from_snapshot(self, snapshot: dict) -> tuple[SortedDict, SortedDict]:
        """
        Create two sorted dictionaries from the json response snapshot.
        """

        data = snapshot['data'][0]

        bids = SortedDict({bid['price']:bid['qty'] for bid in data['bids']})
        asks = SortedDict({ask['price']:ask['qty'] for ask in data['asks']})

        return bids, asks

    
    def _verify_checksum(self, checksum: int) -> bool:
        """"
        Verify if the checksum of the local books coincides with the 
        checksum `checksum` provided by the Kraken API.
        """

        checksum_str = ""

        for price, qty in list(self.asks.items())[:10]:

            price = self._format_kraken_str(price, 1)
            qty = self._format_kraken_str(qty, 8)
            checksum_str += price + qty

        for price, qty in list(reversed(self.bids.items()))[:10]:

            price = self._format_kraken_str(price, 1)
            qty = self._format_kraken_str(qty, 8)
            checksum_str += price + qty

        return checksum == crc32(checksum_str.encode('utf-8'))




class KrakenL3Socket(KrakenSocket):
    """
    Kraken Level 3 Websocket to connect to the Kraken API. 
    Adds another level of granularity ot the KrakenL2Socket,
    i.e. shows orders in the visible book.

    =====
    Source: https://docs.kraken.com/api/docs/websocket-v2/level3
    """

    BOOK_DEPTHS = [10, 100, 1000]

    def __init__(self, symbol: str, depth: int = 10,
                 on_invalid: str = 'raise', debug: bool = False,
                 checksum_freq: int = 10,
                 api_key: str = None, api_secret_key: str = None):

        self.symbol = self._ensure_pair_validity(symbol, on_invalid=on_invalid)
        self.token = get_token(api_key, api_secret_key)

        self.bids = SortedDict()
        self.asks = SortedDict()

        if depth not in KrakenL3Socket.BOOK_DEPTHS:
            raise ValueError(f"The book depth has to be in {KrakenL3Socket.BOOK_DEPTHS}.")
        
        self.depth = depth
    
        super().__init__(auth=True, debug=debug)

        self.count = 0
        self.checksum_freq = checksum_freq


    def _on_close(self, ws: websocket.WebSocket, close_status_code: int, close_msg: str):
        """
        Handle the closing of the websocket.
        """

        print("Closing the Kraken L3 socket...")
        print(f"{self.count} ticker messages received and handled.")


    def _on_error(self, ws: websocket.WebSocket, error: str):
        """
        Handle the error of the websocket.
        """

        print(f"\nReceived error: {error}\n")


    def _on_message(self, ws: websocket.WebSocket, message: str):
        """
        **This function provides the main interface to parse the responses from the server.**

        Handle and parse the incoming server response `message`.
        """

        response = json.loads(message)

        #LOGIC TO MAINTAIN THE ORDER BOOK
        #skip status and hearbeat messages
        if response.get('channel', "") == 'status' or response.get('channel', "") == 'heartbeat':
            pass

        else:
            if self.count == 0: # skip subscription ack.
                pass

            else:
                data = response['data'][0]
                checksum = data['checksum']

                if response['type'] == 'snapshot':
                    self.bids, self.asks = self._create_book_from_snapshot(response)                  

                else:
                    bid_orders = data['bids']
                    ask_orders = data['asks']

                    for bid_order in bid_orders:

                        oid = bid_order['order_id']
                        oprice = bid_order['limit_price']
                        oqty = bid_order['order_qty']

                        match(bid_order['event']):

                            case 'add':
                                oprice_level = self.bids.get(oprice, None)

                                if not oprice_level:
                                    self.bids[oprice] = {oid: oqty}
                                else:
                                    self.bids[oprice][oid] = oqty

                            case 'modify':
                                self.bids[oprice][oid] = oqty

                            case 'delete':
                                del self.bids[oprice][oid]

                                if not self.bids[oprice]:
                                    del self.bids[oprice]

                            case _:
                                raise ValueError("the order field 'event' should be ",
                                        f"'add', 'modify' or 'delete, but is {ask_order['event']}")
                    

                    for ask_order in ask_orders:

                        oid = ask_order['order_id']
                        oprice = ask_order['limit_price']
                        oqty = ask_order['order_qty']

                        match(ask_order['event']):

                            case 'add':
                                oprice_level = self.asks.get(oprice, None)

                                if not oprice_level:
                                    self.asks[oprice] = {oid: oqty}
                                else:
                                    self.asks[oprice][oid] = oqty

                            case 'modify':
                                self.asks[oprice][oid] = oqty

                            case 'delete':
                                del self.asks[oprice][oid]

                                if not self.asks[oprice]:
                                    del self.asks[oprice]

                            case _:
                                raise ValueError("the order field 'event' should be ",
                                        f"'add', 'modify' or 'delete, but is {ask_order['event']}")


                    overflow_asks = len(self.asks) - self.depth
                    overflow_bids = len(self.bids) - self.depth

                    for ask_price in reversed(self.asks):

                        if overflow_asks == 0:
                            break

                        overflow_asks -= 1
                        del self.asks[ask_price]
                 
                    for bid_price in self.bids:

                        if overflow_bids == 0:
                            break

                        overflow_bids -= 1
                        del self.bids[bid_price]


                if self.count % self.checksum_freq == 0:
                
                    checksum = data['checksum']

                    if not self._verify_checksum(checksum):
                        #TODO: at this point you would probably want to rebuild the book, instead of throwing an Error.
                        raise InvalidChecksumError("The checksum verification failed.") 
                
            self.count += 1
    

    def _on_open(self, ws: websocket.WebSocket):
        """
        Handles the opening of the socket and the sending of the subscription request.
        """

        print("Kraken L3 Socket opened.")

        subscription_params = {
            'channel': 'level3',
            'symbol': self.symbol,
            'depth': self.depth,
        }

        self.ws.send(self._json_subcribe_message(subscription_params, token=self.token))         

    
    def _create_book_from_snapshot(self, snapshot: str) -> tuple[SortedDict, SortedDict]:
        """
        Create two sorted dictionaries (bids and asks) from the json response snapshot.
        """

        data = snapshot['data'][0]

        asks = SortedDict()
        bids = SortedDict()

        price = -1
        orders = {}

        for bid in data['bids']:

            curr_price = bid['limit_price']
            curr_qty = bid['order_qty']
            curr_id = bid['order_id']

            if price != curr_price:
                bids[price] = orders
                price = curr_price
                orders = {curr_id: curr_qty}
            else:
                orders[curr_id] = curr_qty

        bids[price] = orders
        del bids[-1]

        price = -1

        for ask in data['asks']:

            curr_price = ask['limit_price']
            curr_qty = ask['order_qty']
            curr_id = ask['order_id']

            if price != curr_price:
                asks[price] = orders
                price = curr_price
                orders = {curr_id: curr_qty}

            else:
                orders[curr_id] = curr_qty
        
        asks[price] = orders
        del asks[-1]

        return bids, asks


    def _verify_checksum(self, checksum: int) -> bool:
        """"
        Verify if the checksum of the local books coincides with the 
        checksum `checksum` provided by the Kraken API.
        """

        checksum_str = ""

        for price, orders in list(self.asks.items())[:10]:

            price = self._format_kraken_str(price, 1)

            for qty in orders.values(): 

                qty = self._format_kraken_str(qty, 8)
                checksum_str += price + qty

        for price, orders in list(reversed(self.bids.items()))[:10]:

            price = self._format_kraken_str(price, 1)

            for qty in orders.values():
                qty = self._format_kraken_str(qty, 8)

                checksum_str += price + qty

        return checksum == crc32(checksum_str.encode('utf-8'))


