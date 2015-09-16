# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PervasiverhizomeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url_title = scrapy.Field()
    link = scrapy.Field()
    contentTracker = scrapy.Field()
    contentTracker_URL=scrapy.Field()
    pass
