# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Ku137Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    imgtitle= scrapy.Field()
    imgname = scrapy.Field()
    imgurl = scrapy.Field()
    page = scrapy.Field()
