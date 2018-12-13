# -*- coding: utf-8 -*-
import scrapy
from GetProxy.items import GetproxyItem


class KdlSpider(scrapy.Spider):
    name = 'kdl'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['https://www.kuaidaili.com/free/']

    def parse(self, response):
        proxy_lists = response.xpath('//*[@id="list"]/table/tbody/tr')
        for proxy in proxy_lists:
            item = GetproxyItem()
            item['ip'] = proxy.xpath('.//td[1]/text()').extract_first()
            item['port'] = proxy.xpath('.//td[2]/text()').extract_first()
            item['kind'] = proxy.xpath('.//td[4]/text()').extract_first()
            item['addr'] = proxy.xpath('.//td[5]/text()').extract_first()
            item['speed'] = proxy.xpath('.//td[6]/text()').extract_first()
            item['lastcheck'] = proxy.xpath('.//td[7]/text()').extract_first()
            yield item
        return None
