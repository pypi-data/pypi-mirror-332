from pydantic import BaseModel


class RequestOptions(BaseModel):
    method: str
    path: str
    json: dict
    params: dict

    def __init__(self, method: str, path: str, json: dict, params: dict):
        self.method = method
        self.path = path
        self.json = json
        self.params = params

    @classmethod
    def construct(cls, method: str, path: str, json: dict, params: dict):
        return cls(method, path, json, params)
