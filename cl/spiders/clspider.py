# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from cl.items import ClItem
from scrapy.selector import Selector


class ClspiderSpider(CrawlSpider):
    name = 'clspider'
    allowed_domains = ['cl.beett.pw']
    rules = (
        Rule(LinkExtractor(allow='cl.beett.pw/htm_data',
                           restrict_xpaths='//td[@style="text-align:left;padding-left:8px"]/h3/a'),
             callback='parse_item', follow=True),
    )

    def start_requests(self):
        pages = []
        for i in [8, 16]:
            for d in [1, 2]:
                url = 'http://cl.beett.pw/thread0806.php?fid=%d&search=&page=%d' % (i, d)
                page = scrapy.Request(url)
                pages.append(page)
        return pages
    
    def parse_item(self, response):
        sel = Selector(response)
        pic = sel.xpath('//div[@class="tpc_content do_not_catch"]//input/@src').extract()
        item = ClItem()
        item['image_urls'] = pic
        yield item
