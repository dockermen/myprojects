from time import time
from typing_extensions import Required
import scrapy


class BqgSpider(scrapy.Spider):
    name = 'bqg'
    allowed_domains = ['xbiquge.la']
    start_urls = ['http://www.xbiquge.la/10/10489/']

    def parse(self, response):
        title = response.selector.xpath('//div[@id="list"]//dd[2]/a/text()').get()
        next_url = response.selector.xpath('//div[@id="list"]//dd[2]/a/@href').get()
        yield scrapy.Request(response.urljoin(next_url),meta={'title':title},dont_filter=True)


    # def parse_info(self,response):
    #     title = response.request.meta.get('title')
    #     print(title,"----------------")