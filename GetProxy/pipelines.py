# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class GetproxyPipeline(object):
    def open_spider(self, spider):
        self._file = open('proxy.svc', 'w', encoding='utf-8')
        self._file.write('ip,port,kind,addr,speed,lastcheck\n')

    def close_spider(self, spider):
        self._file.close()

    def process_item(self, item, spider):
        self._file.write('{},{},{},{},{},{}\n'.format(item['ip'], item['port'], item['kind'], item['addr'],
                                                    item['speed'], item['lastcheck']))
        return item
