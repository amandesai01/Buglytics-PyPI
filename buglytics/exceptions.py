class BuglyticsException(Exception):
    def __str__(self):
        "Base Exception"

class TokenInvalidException(Exception):
    def __str__(self):
        "Token submitted is not valid OR correct access rights not granted."

class ConnectionNotEstablishedException(Exception):
    def __str__(self):
        "Couldn't establish connection to server. Check URL and connectivity."

class RequestNotReportedException(Exception):
    def __str__(self):
        "Unable to report request"