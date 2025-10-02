from dataclasses import dataclass


@dataclass
class ScanItem:
    name: str
    price: float
    description: str
    product_url: str


@dataclass
class ItemListPage:
    product_urls: list[str]
    page_url: str
