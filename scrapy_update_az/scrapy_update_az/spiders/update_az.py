import scrapy


class UpdateAzSpider(scrapy.Spider):
    name = 'update_az'
    start_urls = ['https://azaforum.com/download/CHAMPIONS%20(Sat%C3%A9lite)/?C=M;O=A']

    def parse(self, response):
        for update in response.css("table tr"):
            #if not contains  word 'Champions' ignore            
            yield {
                "name": update.css('a::text').get(),
                "last modified": update.css('td:nth-child(3) ::text').get()
            }
