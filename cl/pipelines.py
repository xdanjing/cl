# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request


class ClPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split('/')[-2:]
        image_file_name = '_'.join(image_guid)
        return '%s' % image_file_name

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url)
