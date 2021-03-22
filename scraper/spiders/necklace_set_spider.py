import scrapy


class NecklaceSetSpider(scrapy.Spider):
    name = "necklace_set"
    start_urls = [
        'https://www.houseofindya.com/zyra/necklace-sets/cat'
    ]

    def parse(self, response):
        for items in response.css("div.catgList ul"):
            for item in items.css("li"):
                yield {
                    'description': item.css("div.catgName p::text").get(),
                    'price': item.css("div.catgName span::text").get()[1:],
                    'image': item.css('img::attr(data-original)').get()
                }
