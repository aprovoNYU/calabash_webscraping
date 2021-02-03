import scrapy
from scrapy import Selector
from calabash.items import CalabashItem, CalabashTitle

class ContributorsSpider(scrapy.Spider):
    name = 'contributors'
    allowed_domains = ['http://www.nyu.edu/calabash/']
    start_urls = [
    				'http://www.nyu.edu/calabash/vol1no1/contributors_vol1no1.shtml',
      				'http://www.nyu.edu/calabash/vol1no2/contributors_vol1no2.shtml',
    				'http://www.nyu.edu/calabash/vol2no1/contributors_vol2no1.shtml',
    				'http://www.nyu.edu/calabash/vol2no2/contributors_vol2no2.shtml',
    				'http://www.nyu.edu/calabash/contributors.shtml',

    				]


    def parse(self, response):
        record=CalabashItem()
        #doc = response.body
        url = response.url
        #print(doc)
        print(url)
        #calabashpagehtmlselector = Selector(text=doc,type="html")
        for p in response.xpath("//p"):
            record['issueurl'] = url
            #record['section'] = p.xpath("[@class='tocsection' or @class='highlights']") 
            # print(section)     	
            record['author'] = p.xpath("./span[@class='author']/text()").get()
            record['authorbio'] = p.xpath("./span[@class='author']/../text()").get()
            yield record



