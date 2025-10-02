import scrapy


class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["scan.co.uk"]

    url: str = (
        "https://www.scan.co.uk/products/powercolor-radeon-rx-9060-xt-reaper-8gb-gddr6-graphics-card-rdna4-2048-streams-3130mhz-boost"
    )

    async def start(self):
        yield scrapy.Request(url=self.url, callback=self.parse)

    async def parse(self, response):
        yield {
            "name": response.css("h1[itemprop='name']::text").get(),
            "price": response.css("span[itemprop='price']::attr(content)").get(),
            "description": response.css("h2[itemprop='description']::text").get().strip().replace("\n", ""),
            "url": response.url,
        }
