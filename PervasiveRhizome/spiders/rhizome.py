import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import *
from PervasiveRhizome.items import PervasiverhizomeItem

class RhizomeSpider(scrapy.Spider):
    name = "rhizome"
    allowed_domains = ["amazon.com"]
    start_urls = [
        "http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=raspberry+pi"
    ]

    def parse(self, response):
        print "IN PARSE DRESS"      
        item = PervasiverhizomeItem()
        sel=Selector(response)
        item['url_title'] = sel.xpath('///h2[@class="a-size-base a-color-null s-inline s-access-title a-text-normal"]/text()')
        yield item
