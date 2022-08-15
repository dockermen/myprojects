import scrapy


class Zol3Spider(scrapy.Spider):
    name = 'zol3'
    allowed_domains = ['zol.com.cn']
    start_urls = ['https://desk.zol.com.cn/bizhi/9790_118029_2.html']

    def parse(self, response):
        img_url = response.xpath('//img[@id="bigImg"]/@src').get()
        img_name = response.xpath('string(//h3)').get().strip().replace('\r\n\t\t','').replace('/','_')
        yield {
            'img_url':img_url,
            'img_name':img_name
        }
        next_url = response.xpath('//a[@id="pageNext"]/@href').get()
        if next_url == 'javascript:;':return
        full_url = response.urljoin(next_url)
        yield scrapy.Request(full_url)
