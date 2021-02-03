# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class CalabashTitle(scrapy.Item):
    pdfname = scrapy.Field()
    title = scrapy.Field()

class CalabashItem(scrapy.Item):
    # define the fields for your item here like:
    author = scrapy.Field()
    authorbio = scrapy.Field()
    titlegroup = scrapy.Field()
    pdfname = scrapy.Field()
    title = scrapy.Field()
    issueurl = scrapy.Field()
    section = scrapy.Field()