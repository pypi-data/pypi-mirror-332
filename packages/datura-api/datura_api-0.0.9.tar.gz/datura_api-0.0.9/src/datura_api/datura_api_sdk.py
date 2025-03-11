import requests
from .protocol import (
    AISearchPayload,
    TwitterSearchPayload,
    WebSearchPayload,
    WebLinksPayload,
    TwitterLinksPayload,
    AISearchResponse,
    WebLinksSearchResponse,
    TwitterLinksSearchResponse,
    BasicTwitterSearchResponse,
    BasicWebSearchResponse,
)
from typing import Union


BASE_URL = "https://apis.datura.ai"
AUTH_HEADER = "Authorization"


class DaturaApiSDK:
    def __init__(self, api_key: str):
        self.client = requests.Session()
        self.client.headers.update({AUTH_HEADER: api_key})

    def handle_request(self, request_func, *args, **kwargs):
        try:
            response = request_func(*args, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(
                f"Server Error: {http_err.response.status_code} - {http_err.response.text}"
            )
            raise
        except requests.exceptions.RequestException as err:
            print(f"Network Error: {err}")
            raise

    def ai_search(self, payload: AISearchPayload) -> Union[AISearchResponse, dict, str]:
        return self.handle_request(
            self.client.post, f"{BASE_URL}/desearch/ai/search", json=payload
        )

    def search_web_links(self, payload: WebLinksPayload) -> WebLinksSearchResponse:
        return self.handle_request(
            self.client.post,
            f"{BASE_URL}/desearch/ai/search/links/web",
            json=payload,
        )

    def search_twitter_links(
        self, payload: TwitterLinksPayload
    ) -> TwitterLinksSearchResponse:
        return self.handle_request(
            self.client.post,
            f"{BASE_URL}/desearch/ai/search/links/twitter",
            json=payload,
        )

    def basic_twitter_search(
        self, payload: TwitterSearchPayload
    ) -> BasicTwitterSearchResponse:
        return self.handle_request(
            self.client.post, f"{BASE_URL}/twitter", json=payload
        )

    def basic_web_search(self, payload: WebSearchPayload) -> BasicWebSearchResponse:
        return self.handle_request(self.client.get, f"{BASE_URL}/web", params=payload)
