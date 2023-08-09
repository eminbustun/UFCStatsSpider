# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UfcstatScraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass

class FightItem(scrapy.Item):
    win = scrapy.Field()
    lose = scrapy.Field()
    draw1 = scrapy.Field()
    draw2 = scrapy.Field()
    nc1 = scrapy.Field()
    nc2 = scrapy.Field()
    weight_class = scrapy.Field()
    method = scrapy.Field()
    endWith = scrapy.Field()
    roundd = scrapy.Field()
    time = scrapy.Field()
