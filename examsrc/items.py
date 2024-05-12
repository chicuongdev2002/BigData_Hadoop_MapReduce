# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class examsrcItem(scrapy.Item):
    title20020331 = scrapy.Field() # Title
    genre20020331 = scrapy.Field() # Genre
    type20020331 = scrapy.Field() # Type
    priceex20020331 = scrapy.Field() # Price exclude tax
    pricein20020331 = scrapy.Field() # Price include tax
    tax20020331 = scrapy.Field() # Tax
    ava20020331 = scrapy.Field() # Availability
    review20020331 = scrapy.Field() # Number of reviews
