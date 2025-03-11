import httpx

from ._exceptions import APIExceptions


class SyncHttpClient:
    def __init__(self, api_key: str, base_url: str | None = None) -> None:
        self.api_key = api_key
        self.base_url = "https://api.creduse.com" if base_url is None else base_url
        self.http_client = httpx.Client()

        self.http_client.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def post(self, endpoint: str, body: dict):
        url = f"{self.base_url}{endpoint}"
        response = self.http_client.post(url, json=body)
        if response.status_code != 200:
            raise APIExceptions.from_response(response)
        return response.json()

    def get(self, endpoint: str, body: dict):
        url = f"{self.base_url}{endpoint}"
        response = self.http_client.request("GET", url, json=body)
        if response.status_code != 200:
            raise APIExceptions.from_response(response)
        return response.json()


class AsyncHttpClient:
    def __init__(self, api_key: str, base_url: str | None = None) -> None:
        self.api_key = api_key
        self.base_url = "https://api.creduse.com" if base_url is None else base_url

    async def post(self, endpoint: str, body: dict):
        url = f"{self.base_url}{endpoint}"
        async with httpx.AsyncClient() as client:
            client.headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            }
            response = await client.post(url, json=body)
        if response.status_code != 200:
            raise APIExceptions.from_response(response)
        return response.json()

    async def get(self, endpoint: str, body: dict):
        url = f"{self.base_url}{endpoint}"
        async with httpx.AsyncClient() as client:
            client.headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            }
            response = await client.request("GET", url, json=body)
        if response.status_code != 200:
            raise APIExceptions.from_response(response)
        return response.json()
