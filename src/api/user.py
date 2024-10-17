import time
import base64
import hashlib
import hmac
import urllib.request
import json
import os
from dotenv import load_dotenv


def get_token() -> str:
    """
    Get the Kraken Token associated with the user with the API keys provided in the .env file.

    ======
    Source: edited from: https://support.kraken.com/hc/en-us/articles/360034437672-How-to-retrieve-a-WebSocket-authentication-token-Example-code-in-Python-3
    """

    load_dotenv()
    api_key = os.getenv('API_KEY')
    api_private_key = os.getenv('API_PRIVATE_KEY')

    api_path = '/0/private/GetWebSocketsToken'
    api_nonce = str(int(time.time()*1000))
    api_post = 'nonce=' + api_nonce

    api_sha256 = hashlib.sha256(api_nonce.encode('utf-8') + api_post.encode('utf-8'))
    api_hmac = hmac.new(base64.b64decode(api_private_key), api_path.encode('utf-8') + api_sha256.digest(), hashlib.sha512)

    api_signature = base64.b64encode(api_hmac.digest())

    api_request = urllib.request.Request('https://api.kraken.com/0/private/GetWebSocketsToken', api_post.encode('utf-8'))
    api_request.add_header('API-Key', api_key)
    api_request.add_header('API-Sign', api_signature)
    api_response = urllib.request.urlopen(api_request).read().decode()

    return json.loads(api_response)['result']['token']