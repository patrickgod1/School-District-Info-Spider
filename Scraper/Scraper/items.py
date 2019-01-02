# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class ScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    Name = scrapy.Field()
    City = scrapy.Field()
    County = scrapy.Field()
    Telephone = scrapy.Field()
    DistrictURL = scrapy.Field()
    SchoolCount= scrapy.Field()
    Grades = scrapy.Field()

