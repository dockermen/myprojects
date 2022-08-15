# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
import scrapy

class MongoPipeline:

    def open_spider(self,spider):
        scrapy.Request('http://www.cwl.gov.cn/')
        print("初次请求获取Cookie")
        self.client = MongoClient()
        self.ssq = self.client.caipiao.ssq

    def process_item(self, item, spider):
        self.ssq.insert_one(item)
        return item

    def close_spider(self,spider):
        self.client.close()
