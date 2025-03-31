class ResponseBase():
    def __init__(self, code, message):
        self.message = message
        self.code = code    