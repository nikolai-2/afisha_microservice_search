class ResponseError(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg

    def to_dict(self):
        return dict(
            code=self.code,
            msg=self.msg
        )