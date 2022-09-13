# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BradvisorsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    address = scrapy.Field()
    city = scrapy.Field()
    city_state = scrapy.Field()
    zip = scrapy.Field()
    description = scrapy.Field()
    size_summary = scrapy.Field()
    item_url = scrapy.Field()
    property_sub_type_name = scrapy.Field()
    sale = scrapy.Field()
    sublease = scrapy.Field()
