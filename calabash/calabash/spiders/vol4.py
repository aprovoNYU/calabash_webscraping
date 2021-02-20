import scrapy
from scrapy import Selector
from calabash.items import CalabashItem, CalabashTitle

class Vol4Spider(scrapy.Spider):
    name = 'vol4'
    allowed_domains = ['www.nyu.edu/calabash/']
    start_urls = [  'http://www.nyu.edu/calabash/vol4no1/',
                    'http://www.nyu.edu/calabash/vol4no2/',
                    'http://www.nyu.edu/calabash/',

    				]

    def parse(self, response):
    	record=CalabashItem()
    	titlegroup=CalabashTitle()

    	# calabashpagehtml = response.xpath("/html/body").getall()
    	# doc = calabashpagehtml[0]
    	doc = response.body
    	url = response.url
    	print(doc)
    	print(url)
    	calabashpagehtmlselector = Selector(text=doc,type="html")
    	# author = calabashpagehtmlselector.xpath("//td/p/span[@class='author']/text()")
    	# print(author)
    	for p in calabashpagehtmlselector.xpath("//div"):
        	record['issueurl'] = url
        	#record['section'] = p.xpath("[@class='tocsection' or @class='highlights']") 
        	# print(section)     	
        	record['author'] = p.xpath("./*[@class='author']/text()").get()

        	for articletitle in p.xpath("./*[@class='articleTitle' or @class='articleTitle1']/a"):
	        	# titlepair={}
	        	# #print(articletitle)#item['titlepair'] = {
		        # titlepair['pdfname'] = articletitle.xpath("./@href").getall()
		       
		        # #print(pdfname)
		        # titlepair['title'] = articletitle.xpath("./text()").getall()
		        
		        # #print(title)
		        # # cleantitle = title.replace("\n", "")
		        # # cleantitle = ' '.join(cleantitle.split())
		        # # print(cleantitle)
		        # # titlepair['pdfname'] = pdfname
		        # # titlepair['title'] = cleantitle
		        # #print(titlepair)
	        	# #print(title)
	        	# #print(author)
	        	# record['titlegroup'] = titlepair

	        	record['pdfname'] = articletitle.xpath("./@href").getall()
		       
		        #print(pdfname)
		        record['title'] = articletitle.xpath("./text()").getall()
		        

        		yield record	


        # for p in response.xpath("//td/p"):
        # 	yield {
        # 		'pdfname' : p.xpath("./span[@class='title' or 'titleh']/a/@href").extract(),
        # 	#print(pdfname)
        # 		'title' : p.xpath("./span[@class='title' or 'titleh']/a/text()").extract(),
        # 	#print(title)
        # 		'author' : p.xpath("./span[@class='author']/text()").extract_first()
        # 	#print(author)
        # 	}