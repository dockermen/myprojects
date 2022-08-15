import scrapy
from json import loads


class SsqSpider(scrapy.Spider):
    name = 'ssq'
    allowed_domains = ['cwl.gov.cn']
    start_urls = ['http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=ssq&issueCount=30&issueStart=&issueEnd=&dayStart=&dayEnd=']


    '''
    def start_requests(self):
        scrapy.Request('http://www.cwl.gov.cn/')
        yield scrapy.Request('http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=ssq&issueCount=30&issueStart=&issueEnd=&dayStart=&dayEnd=',dont_filter=True)
    '''

    def parse(self, response):
        #if "查询成功" in response.text:
        data = loads(response.text)
        for d in data.get('result'):
            yield {
                "code":d.get('code'),
                "red":d.get('red'),
                "blue":d.get('blue')
                }


'''        try:
            data = loads(response.text)
            for d in data.get('result'):
                yield {
                    "code":d.get('code'),
                    "red":d.get('red'),
                    "blue":d.get('blue')
                    }
        except Exception as e:
            pass

'''



