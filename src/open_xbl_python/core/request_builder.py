import aiohttp

from ..utils.endpoints import BASE_URL


class RequestBuilder:
    def __init__(self, api_key: str, proxy: str, language: str):
        self.api_key = api_key
        self.proxy = proxy
        self.language = language

    async def get(self, **kwargs):
        """Handles the GET requests and returns the parsed objects.

        :param kwargs: The query parameters to add to the request.

        :returns: Formatted Objects from HTTP Response.

        """
        headers = {"X-Authorization": self.api_key, "Accept-Language": self.language}
        if "headers" in kwargs.keys():
            headers = headers | kwargs["headers"]

        params = None
        if "params" in kwargs.keys():
            params = kwargs["params"]

        data = None
        if "data" in kwargs.keys():
            data = kwargs["data"]

        async with aiohttp.ClientSession() as session:
            async with session.get(f"{BASE_URL}{kwargs['endpoint']}", headers=headers, params=params, data=data) as resp:
                return await resp.json()
