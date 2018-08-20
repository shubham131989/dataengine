




import scrapy

class JustdialItem(scrapy.Item):
    sourceId = scrapy.Field()
    #datetime = scrapy.Field()
    name = scrapy.Field()
    phoneNo = scrapy.Field()
    whatsappNo = scrapy.Field()
    address = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    location = scrapy.Field()
    category = scrapy.Field()
    totalReviews = scrapy.Field()
    timings = scrapy.Field() 
    rating = scrapy.Field()

class IndiamartItem(scrapy.Item):
    sourceId = scrapy.Field()
    name = scrapy.Field()
    phoneNo = scrapy.Field()
    location = scrapy.Field()
    url = scrapy.Field()
    


             
             
              
