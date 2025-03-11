from pydantic import BaseModel

from fitrequest.client import FitRequest
from fitrequest.decorators import cli_method, fit


class Item(BaseModel):
    item_id: int
    item_name: str
    detail_id: int


class ItemDetails(BaseModel):
    detail_id: int
    detail: str
    item_id: int
    item_name: str


class RestApiClient(FitRequest):
    """Awesome class generated with fitrequest."""

    client_name = 'rest_api'
    base_url = 'https://test.skillcorner.fr'
    method_docstring = 'Calling endpoint: {endpoint}'

    @fit(endpoint='/items/')
    def get_items(self) -> list[Item]: ...

    @fit(endpoint='/items/{item_id}')
    def get_item(self, item_id: str) -> Item: ...

    @fit(endpoint='/items/{item_id}/details/{detail_id}')
    def get_item_details(self, item_id: str, detail_id: str) -> ItemDetails: ...

    @cli_method
    def get_details(self) -> list[ItemDetails]:
        """Return list of ItemDetails."""
        return [self.get_item_details(item.item_id, item.detail_id) for item in self.get_items()]


client_cli = RestApiClient()
