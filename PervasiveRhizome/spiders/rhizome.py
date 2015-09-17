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
    rules = (Rule (SgmlLinkExtractor(allow=("a-link-normal s-access-detail-page  a-text-normal", ),restrict_xpaths=('//p[@class="nextpage"]',))
    , callback="parse", follow= True),
    )

    def parse(self, response):
        sel=Selector(response)
        items= []
        titles=sel.xpath('//a[@class="a-link-normal s-access-detail-page  a-text-normal"]/@title')
        for title in titles:
            item = PervasiverhizomeItem()
            item['url_title'] = title.extract()
            items.append(item)
        return items
