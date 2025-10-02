from attrs import field
from web_poet import Returns, WebPage, field, handle_urls

from base.items import ScanItem


def clean_newlines(s: str) -> str:
    return s.replace("\n", "")


@handle_urls("scan.co.uk/products/")
class ProductPage(WebPage, Returns[ScanItem]):
    class Processors:
        name = [clean_newlines, str.strip]
        description = [clean_newlines, str.strip]

    @field
    def name(self):
        return self.css("h1[itemprop='name']::text").get()

    @field
    def price(self):
        return self.css("span[itemprop='price']::attr(content)").get()

    @field
    def description(self):
        return self.css("h2[itemprop='description']::text").get()

    @field
    def product_url(self):
        return str(self.response.url)
