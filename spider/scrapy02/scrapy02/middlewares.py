# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

from scrapy.http.response.html import HtmlResponse

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

class SeleniumDownloaderMiddleware:

    def process_request(self, request, spider):
        HtmlResponse.
