import scrapy



from  justdial2 import items





class IndiamartSpider(scrapy.Spider):
    name = 'indiamart'
    allowed_domains = ['indiamart.com']
    
    def __init__(self,keyword='',**kwargs):
        #kwargs.pop('_job')
        self.base_urls = 'https://dir.indiamart.com/search.mp?ss={}&pg='.format(keyword)
        self.start_urls = [self.base_urls + str(x) for x in range(1,10)]
        
   
    def parse(self, response):
        quotes = response.xpath('//*[@data-catid]')
        #ts = time.time() 
        #timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        items_list = []

        #links = ('https://dir.indiamart.com/search.mp?ss=bike&pg={}'.format(i))
        

        for pnt in quotes:
            
            item = items.IndiamartItem()
            item['sourceId'] = 1
            item['name'] = str(pnt.xpath('.//*[@class ="nes"]//*[@class = "lcname"]/text()').extract_first())
            item['url'] = str(pnt.xpath('.//*[@class="nes"]//*[@class = "lcname"]/@href').extract_first())
            item['location'] = str(pnt.xpath('.//*[@class="nes"]//*[@data-rlocation]/text()').extract_first())
            item['phoneNo'] = str(pnt.xpath('.//*[@class= "hlb cur"]//*[@class ="ls_co phn bo"]/text()').extract_first())
            items_list.append(item)
        return items_list
            
            


   
 
            
        
