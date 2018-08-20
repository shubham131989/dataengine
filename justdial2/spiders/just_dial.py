# -*- coding: utf-8 -*-
import scrapy
import json

from justdial2 import items


class JustDialSpider(scrapy.Spider):
    name = 'just_dial'
    allowed_domains = ['justdial.com']


    def __init__(self, city='', keyword='',**kwargs):

      #kwargs.pop('_job')
      self.base_url = 'https://t.justdial.com/api/india_api_write/01jan2018/searchziva.php?city={}&area=&lat=&long=&darea_flg=0&case=spcall&stype=category_list&search={}&pg_no='.format(city,keyword)
      self.start_urls = [self.base_url + str(x) for x in range(1,50)]
      self.sr_no = 0



    def parse(self, response):
        json_obj = json.loads(response.body_as_unicode())
        sr_no = 0
        #stop = json_obj['results']['data']
        #while stop != 'null' :
        items_list = []
        


        for i in range(10):
              
              item = items.JustdialItem()
              item['sourceId'] = 2
              item['name'] = str(json_obj['results']['data'][i][1].encode('utf-8'))
              item['address'] = str(json_obj['results']['data'][i][3])
              item['latitude'] = str(json_obj['results']['data'][i][4])
              item['longitude'] = str(json_obj['results']['data'][i][5])
              item['phoneNo'] = str(json_obj['results']['data'][i][23]['t'] + '  '+json_obj['results']['data'][i][23]['m'] + '  ' + json_obj['results']['data'][i][23]['l']) 
              item['totalReviews'] = str(json_obj['results']['data'][i][16])
              item['category'] = str(json_obj['results']['data'][i][14])
              item['timings'] = str(json_obj['results']['data'][i][11]['timing'])
              #Area = json_obj['results']['data'][i][12]
              if 'business'  in str(json_obj['results']['data'][i][12]):
                item['location'] = 'N/A'
              elif item['category'] == str(json_obj['results']['data'][i][12]):
                item['location'] = 'N/A'
              else:
                item['location'] = str(json_obj['results']['data'][i][12])
              #number =  json_obj['results']['data'][i][29][0]['val'])
              item['whatsappNo'] = str(json_obj['results']['data'][i][34][0])
              item['rating'] = str(json_obj['results']['data'][i][7])          
              #self.sr_no += 1 
              #item['datetime'] = timestamp
              items_list.append(item)
                 
        return items_list


              

   

            


