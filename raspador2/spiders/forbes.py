import scrapy 

class ForbesSpider(scrapy.Spider):
    name = 'Forbes'

    def start_requests(self):
        urls = [
            'https://forbes.com.br/forbes-mulher/2023/02/mulheres-de-sucesso-2023-veja-quem-sao-as-10-escolhidas/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for li in response.css('.stage > ul > li'):
            yield {
                'img': li.css("img::attr(data-lazy-src)").get(),
                'text': li.css("h2::text").get(),
        }
