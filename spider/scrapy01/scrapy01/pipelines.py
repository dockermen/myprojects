# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
'''class Scrapy01Pipeline:
    def process_item(self, item, spider):
        return item'''
#class MyImagePipeline(ImagesPipeline):
class XSPipeline:
    def open_spider(self, spider):
        self.file = open('xs.txt','w',encoding='utf-8')


    def process_item(self, item, spider):
        self.file.write(item.get('title'))
        self.file.write('\n')
        return '追加成功'

    def close_spider(self,spider):
        self.file.close()

    # def get_media_requests(self, item, info):
    #     name = item.get('img_name')
    #     return Request(item.get('img_url'),meta={'name':name})

    # def file_path(self, request, response=None, info=None, *, item=None):
    #     name = request.meta.get('name')
    #     return f'{name}.jpg'