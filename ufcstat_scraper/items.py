# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Identity, TakeFirst, Compose, MapCompose, Join

STR_toInt = Compose(TakeFirst(), int)
STR_toFloat = Compose(TakeFirst(), float)


def stripPercent(str_input):
    number = str_input.strip('%')
    return float(number) / 100


class UfcstatScraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass

class FightItem(scrapy.Item):
    event = scrapy.Field()
    date = scrapy.Field()
    location = scrapy.Field()
    fighter1 = scrapy.Field()
    fighter1ID = scrapy.Field()
    fighter2ID = scrapy.Field()
    fighter2 = scrapy.Field()
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


class FighterSummaryItem(scrapy.Item):
    # define the fields for your item here like:
    fighter_id = scrapy.Field(output_processor=TakeFirst())
    name = scrapy.Field(output_processor=TakeFirst())
    height = scrapy.Field(output_processor=TakeFirst())
    weight = scrapy.Field(output_processor=TakeFirst())
    reach = scrapy.Field(output_processor=TakeFirst())
    stance = scrapy.Field(output_processor=TakeFirst())
    dob = scrapy.Field(output_processor=TakeFirst())
    #active = scrapy.Field(output_processor=TakeFirst())
    n_win = scrapy.Field(output_processor=STR_toInt)
    n_loss = scrapy.Field(output_processor=STR_toInt)
    n_draw = scrapy.Field(output_processor=STR_toInt)
    sig_str_land_pM = scrapy.Field(output_processor=STR_toFloat)
    sig_str_land_pct = scrapy.Field(
        output_processor=Compose(TakeFirst(), stripPercent))
    sig_str_abs_pM = scrapy.Field(output_processor=STR_toFloat)
    sig_str_def_pct = scrapy.Field(
        output_processor=Compose(TakeFirst(), stripPercent))
    td_avg = scrapy.Field(output_processor=STR_toFloat)
    td_land_pct = scrapy.Field(
        output_processor=Compose(TakeFirst(), stripPercent))
    td_def_pct = scrapy.Field(
        output_processor=Compose(TakeFirst(), stripPercent))
    sub_avg = scrapy.Field(output_processor=STR_toFloat)