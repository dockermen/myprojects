import scrapy


class Zol1Spider(scrapy.Spider):
    name = 'zol1'
    allowed_domains = ['zol.com.cn']
    start_urls = ['https://desk.zol.com.cn/bizhi/9790_118029_2.html']

    def parse(self, response):
        img_url = response.xpath('//img[@id="bigImg"]/@src').getall()
        yield {
            'image_urls':img_url
        }
