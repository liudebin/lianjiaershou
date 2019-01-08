# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    house_code = scrapy.Field()
    community_code = scrapy.Field()
    community_link = scrapy.Field()
    community = scrapy.Field()
    town_link = scrapy.Field()
    town_disc = scrapy.Field()
    house_info = scrapy.Field()
    chan_quan = scrapy.Field()
    follow_info = scrapy.Field()
    tags = scrapy.Field()
    price = scrapy.Field()
    price_content = scrapy.Field()
    unit_price = scrapy.Field()
