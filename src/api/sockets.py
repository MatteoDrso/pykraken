
import websocket
import threading
import api.tickers as tickers
import warnings
import json


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


    def _ensure_pair_validity(self, pairs: list[str] | str, on_invalid: str = 'drop') -> int | list[str]:
        """
        Ensure the validity of the passed pair list `pairs` so that they
        coincide with the formatting of Kraken.
        """
        
        ret = list()

        if type(pairs) == str:
            pairs = [pairs]
        elif type(pairs) != list:
            raise TypeError(f"The pairs passed have to be a list of strings or a single string, not {type(pairs)}")

        for pair in pairs:
            if pair in tickers.KRAKEN_PAIRS:
                ret.append(pair)
            else:
                match on_invalid:
                    case 'drop':
                        warnings.warn(f"{pair} not in api.tickers, you might have to update that list.")
                    case 'raise':
                        raise KeyError(f"{pair} not in api.tickers, you might have to update that list.")

        return ret


    def _json_subcribe_message(self, params: dict) -> str:
        """
        Create json message to subscribe to a Kraken API Socket.
        """
        
        json_message = {'method':'subscribe'}
        json_message['params'] = params

        return json.dumps(json_message, indent=4)




class KrakenL1Socket(KrakenSocket):
    """
    Kraken Level 1 Websocket to connect to the Kraken API. 
    Streams ticker/top of the book (best bid/ask) market data and recent trade data.

    =====
    Source: https://docs.kraken.com/api/docs/websocket-v2/ticker
    """

    def __init__(self, symbols: list[str] | str, high_freq: bool = False,
                 on_invalid: str = 'raise', debug: bool = False):

        self.symbols = self._ensure_pair_validity(symbols, on_invalid=on_invalid)
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
            if self.count == 0: # subscription ack.
                pass
            else:
                if (channel := response.get('channel', "")) != 'ticker':
                    warnings.warn(f"expected channel: ticker, got {channel} instead.")
                else:
                    for i, sym in enumerate(self.symbols):
                        data = response['data'][i]
                        print(
                            f"{sym} ${data['last']}, {data['change']} ({data['change_pct']}%)\n" +
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
            'symbol': self.symbols,
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

    def __init__(self, symbols: list[str] | str, depth: int = 10,
                 on_invalid: str = 'raise', debug: bool = False):

        self.symbols = self._ensure_pair_validity(symbols, on_invalid=on_invalid)
        self.event_trigger = 'trades' if high_freq else 'bbo'

        super().__init__(auth=False, debug=debug)

        self.count = 0


    def _on_close(self, ws: websocket.WebSocket, close_status_code: int, close_msg: str):
        pass


    def _on_error(self, ws: websocket.WebSocket, error: str):
        pass


    def _on_message(self, ws: websocket.WebSocket, message: str):
        pass

    
    def _on_open(self, ws: websocket.WebSocket):
        pass    





class KrakenL3Socket(KrakenSocket):
    """
    Kraken Level 3 Websocket to connect to the Kraken API. 
    Adds another level of granularity ot the KrakenL2Socket,
    i.e. shows orders in the visible book.

    =====
    Source: https://docs.kraken.com/api/docs/websocket-v2/level3
    """

    def __init__(self, ):
        pass


    def _on_close(self, ws):
        pass

    def _on_error(self, ws, error):
        pass

    def _on_message(self, ws, message):
        pass
    
    def _on_open(self, ws):
        pass


