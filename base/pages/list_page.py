from web_poet import WebPage, field, handle_urls
from web_poet.pages import Returns

from base.items import ItemListPage


@handle_urls("scan.co.uk")
class ListPage(WebPage, Returns[ItemListPage]):
    @field
    def product_urls(self):
        return self.css("li.product div > a::attr(href)").getall()

    @field
    def page_url(self):
        return str(self.response.url)
