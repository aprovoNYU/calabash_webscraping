import scrapy
from scrapy import Selector
from calabash.items import CalabashItem, CalabashTitle


class Vol45Spider(scrapy.Spider):
    name = 'vol4-5'
    allowed_domains = ['www.nyu.edu/calabash/']
    start_urls = [  #'http://www.nyu.edu/calabash/vol4no1/',
                    #'http://www.nyu.edu/calabash/vol4no2/',
                    'http://www.nyu.edu/calabash/',
    				]
    def parse(self, response):
    	number = 0
    	record=CalabashItem()
    	url = response.url
    	#print(doc)
    	print(url)
    	#calabashpagehtmlselector = Selector(text=doc,type="html")
    	# author = calabashpagehtmlselector.xpath("//td/p/span[@class='author']/text()")
    	# print(author)
    	#print(calabashpagehtmlselector)
    	for div in response.xpath("//div"):
    		#number = number + 1
    		#record ['titlegroup'] = number
    		for article in div.xpath("./*[@class='articleTitle' or @class='articleTitle1' or @class='author']"):

        		record['issueurl'] = url
	        	
	        	record['title'] = article.xpath("./a/text()").getall()
	        	record['pdfname'] = article.xpath("./a/@href").getall()
	        	record['author'] = article.xpath("./text()").getall()
	        	#print(title,pdfname,author)
	        	yield record
