import scrapy
import unidecode

class DataEngineerSalarySpider(scrapy.Spider):
    name = 'data_engineer_salary'
    start_urls = ['https://www.glassdoor.com.br/Sal%C3%A1rios/engenheiro-de-dados-sal%C3%A1rio-SRCH_KO0,19.htm?clickSource=searchBtn']

    def parse(self, response):
        
        for salary in response.css(".css-17435dd"):
            yield {
                "company": unidecode.unidecode(salary.css('.e1aj7ssy3 ::text').get()),
                "rating-company": salary.css('.css-kyx745 ::text').get(),
                "salary-count": unidecode.unidecode(salary.css('.col-lg-auto .css-1b6bxoo ::text').get()),
                "salary": unidecode.unidecode(salary.css('.align-items-baseline .css-g261rn ::text').get()),
                
            }
            
        next_page = response.xpath('//*[@id="nodeReplace"]/div/div/div[1]/div[5]/div[1]/div[3]/div/div[1]/ul/li[5]/a').attrib['href']
        
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
