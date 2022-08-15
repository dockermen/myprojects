import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class XsSpider(CrawlSpider):
    def __init__(self):
        super().__init__()
        self.i = 0
        self.f = 0

    name = 'xs'
    allowed_domains = ['xbiquge.la']
    start_urls = ['https://www.xbiquge.la/10/10489/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=r'//div[@id="list"]/dl/dd[2]/a'), callback='parse_item1', follow=True),
        Rule(LinkExtractor(restrict_xpaths=r'//div[@class="bottem1"]/a[4]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        title = response.xpath('//h1/text()').get()
        content = response.xpath('string(//div[@id="content"])').get()
        xpath_re = ['//div[@id="list"]/dl/dd[2]/a','//div[@class="bottem1"]/a[4]/@href']
        print(f'###{title}##{self.f}')
        self.f += 1
        yield {
            'title':title,
            'content':content
        }

    def parse_item1(self, response):
        print(f'第{self.i}次')
        self.i+= 1
        self.parse_item(response)
