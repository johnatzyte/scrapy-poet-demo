import scrapy

from base.items import ItemListPage, ScanItem


class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["scan.co.uk"]

    url: str = "https://www.scan.co.uk/shop/gaming-and-sims/gpu-amd-gaming/radeon-rx-9060-xt-8gb-graphics-cards"

    async def start(self):
        yield scrapy.Request(url=self.url, callback=self.parse)

    async def parse(self, response, item: ItemListPage):
        for url in item.product_urls:
            yield response.follow(url, callback=self.parse_item)

    async def parse_item(self, _, item: ScanItem):
        yield item
