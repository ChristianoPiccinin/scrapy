import scrapy


class Imdb250Spider(scrapy.Spider):
    name = 'imdb250'
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_td_mv250']

    def parse(self, response):
        for movies in response.css(".lister-list tr"):
            
            yield {
                "title": movies.css('.titleColumn a::text').get(),
                "year": movies.css('.secondaryInfo ::text').get(),
                "rating": movies.css('.ratingColumn strong::text').get()
            }
