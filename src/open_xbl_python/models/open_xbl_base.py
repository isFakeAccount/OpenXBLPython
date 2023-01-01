from ..core.request_builder import RequestBuilder


class OpenXBLBase:
    """Superclass for all the models in OpenXBLPython."""

    def __init__(self, api_key: str, proxy: str, language: str):
        """Initialize a :class:`.OpenXBLBase` instance.

        :param api_key: The api key obtained from https://xbl.io/.
        :param proxy: Proxy URL for connected to API via proxy.
        :param language: Language setting for the API.

        """
        self.api_key = api_key
        self.proxy = proxy
        self.language = language
        self.request_builder = RequestBuilder(api_key=api_key, proxy=proxy, language=language)
