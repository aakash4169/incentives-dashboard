# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 19:31:47 2018

@author: Jacob
"""

import scrapy
# import scrapy_splash

from StateIncentives.items import TestItem

class TestSpider(scrapy.Spider):
    name='TestSpider'
    # allowed_domains=['selectusa.stateincentives.org']
    start_urls=['http://selectusa.stateincentives.org/?referrer=selectusa']
    
    def parse(self, response):
        # real_link='http://selectusa.stateincentives.org/programs/?State=All'
        real_link = 'file:///C:\\Users\\Jacob\\Documents\\UNCC\\Senior Year\\Semester 1\\ITCS 6112\\Final Project\\Scrapy Environment\\StateIncentives\\programslist.html'
        self.log('Entering local file to extract links')
        
        yield scrapy.Request(real_link, callback=self.parse_real)
        
        # yield scrapy_splash.SplashRequest(real_link, self.parse_real, args={'wait':1.5})
    
    def parse_real(self, response):
        test = TestItem()
        filename = 'testRaw.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file%s'%filename)
        test['numRecords'] = response.xpath('//div[@id="ProgramListContainer"]/h2/span/text()').extract()
        self.log('Returning test')
        return test
    