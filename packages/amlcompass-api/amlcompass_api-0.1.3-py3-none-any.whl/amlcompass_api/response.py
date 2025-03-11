import json

class Response:
    def __init__(self, data: dict, status_code: int):
        self.data = data
        self.status_code = status_code

    def to_json(self):
        return json.dumps(self.__dict__)