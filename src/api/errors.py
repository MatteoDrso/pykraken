
class ResponseTypeError(Exception):
    """
    Error that is raised whenever the type of a response is not correct/as expected.
    """

    pass


class InvalidChecksumError(Exception):
    """
    Error that is raised whenever a checksum verification failed.
    """
    
    pass


class APIKeyError(Exception):
    """
    Error that is raised whenever there is a Kraken API Key error.
    """
    
    pass