# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 22:38:09 2018

@author: Jacob Kedar Krevat
"""

import scrapy
from StateIncentives.items import ProgramItem

class StateIncentivesSpider(scrapy.Spider):
    name = 'StateIncentivesSpider'
    start_urls=['http://selectusa.stateincentives.org/?referrer=selectusa']
    
    def parse(self, response):
        # real_link='http://selectusa.stateincentives.org/programs/?State=All'
        real_link = 'file:///C:\\Users\\Jacob\\Documents\\UNCC\\Senior Year\\Semester 1\\ITCS 6112\\Final Project\\Scrapy Environment\\StateIncentives\\programslist.html'
        self.log('Entering local file to extract links')
        
        yield scrapy.Request(real_link, callback=self.parse_real)
        
    def parse_real(self, response):
        links = response.xpath('//div[@id="ProgramListContainer"]/table[@id="programlist"]/tbody/tr/td[@class="progcol"]/a/@href').extract()
        self.log('Successfully parsed links')
        """
        i = 1
        for l in links:
            self.log('http://selectusa.stateincentives.org/programs/' + l)
            i = i + 1
            if i == 20:
                break
        """
        for l in links:
            yield scrapy.Request('http://selectusa.stateincentives.org/programs/'+l, callback=self.parse_program)
            
    def parse_program(self, response):
        program = ProgramItem()
        
        program['program_name'] = self.cleanAndTrim(' '.join(response.xpath('//div[@id="ataglance"]/p[1]/b/text()').extract()))
        program['department'] = self.cleanAndTrim(' '.join(response.xpath('//div[@id="ataglance"]/p[1]/text()').extract()))
        
        otherInfo = '***'.join(response.xpath('//div[@id="ataglance"]/p[2]/text()').extract())
        existingInfo = '***'.join(response.xpath('//div[@id="ataglance"]/p[2]/b/text()').extract())
        
        if 'State' in existingInfo:
            otherInfo = otherInfo[otherInfo.find('***')+3:].strip()
            program['state'] = self.cleanAndTrim(otherInfo[:otherInfo.find('***')])
            otherInfo = otherInfo[otherInfo.find('***')+3:]
            # self.log(otherInfo)
        if 'Category' in existingInfo:
            otherInfo = otherInfo[otherInfo.find('***')+3:].strip()
            program['program_category'] = self.cleanAndTrim(otherInfo[:otherInfo.find('***')])
            otherInfo = otherInfo[otherInfo.find('***')+3:]
        if 'Type' in existingInfo:
            otherInfo = otherInfo[otherInfo.find('***')+3:].strip()
            program['program_type'] = self.cleanAndTrim(otherInfo[:otherInfo.find('***')])
            otherInfo = otherInfo[otherInfo.find('***')+3:]
        if 'Need' in existingInfo:
            otherInfo = otherInfo[otherInfo.find('***')+3:].strip()
            program['business_needs'] = self.cleanAndTrim(otherInfo[:otherInfo.find('***')])
            otherInfo = otherInfo[otherInfo.find('***')+3:]
        if 'Industry' in existingInfo:
            otherInfo = otherInfo[otherInfo.find('***')+3:].strip()
            program['program_industries'] = self.cleanAndTrim(otherInfo[:otherInfo.find('***')])
            otherInfo = otherInfo[otherInfo.find('***')+3:]
        if 'Focus' in existingInfo:
            otherInfo = otherInfo[otherInfo.find('***')+3:].strip()
            program['geographic_focus'] = self.cleanAndTrim(otherInfo[:otherInfo.find('***')])
            otherInfo = otherInfo[otherInfo.find('***')+3:]      
        
        
        program['website'] = response.xpath('//div[@id="ataglance"]/p[3]/a[1]/@href').extract()
        program['additional_website'] = response.xpath('//div[@id="ataglance"]/p[3]/a[2]/@href').extract()
        program['contact_address'] = self.cleanAndTrim(' '.join(response.xpath('//div[@id="contacts"]/p[1]/text()').extract()))
        program['contact_info'] = self.cleanAndTrim(' '.join(response.xpath('//div[@id="contacts"]/p[2]/text()').extract()))
        program['contact_email'] = self.cleanAndTrim(' '.join(response.xpath('//div[@id="contacts"]/p/a/text()').extract()))
        program['program_description'] = self.cleanAndTrim(' '.join(response.xpath('//div[@id="programdetails"]/p[2]/text()').extract()))
        program['program_objectives'] = self.cleanAndTrim(' '.join(response.xpath('//div[@id="programdetails"]/p[4]/text()').extract()))
        program['program_specifics'] = self.cleanAndTrim(' '.join(response.xpath('//div[@id="programdetails"]/p[6]/text()').extract()))
        program['eligibility_requirements'] = self.cleanAndTrim(' '.join(response.xpath('//div[@id="programeligibility"]/p[2]/text()').extract()))
        program['application_information'] = self.cleanAndTrim(' '.join(response.xpath('//div[@id="programeligibility"]/p[4]/text()').extract()))
        program['program_start'] = self.cleanAndTrim(' '.join(response.xpath('//div[@id="statutory"]/p[1]/text()').extract()))
        program['program_finish'] = self.cleanAndTrim(' '.join(response.xpath('//div[@id="statutory"]/p[2]/i/text()').extract()))
        
        i = 3
        if 'Cap' in ' '.join(response.xpath('//div[@id="statutory"]/p[3]/b/text()').extract()):
            program['program_cap'] = self.cleanAndTrim(' '.join(response.xpath('//div[@id="statutory"]/p[3]/text()').extract()))
            i += 1
        program['program_administration_type'] = self.cleanAndTrim(' '.join(response.xpath('//div[@id="statutory"]/p['+ str(i) + ']/text()').extract()))
        i = i + 1
        program['legal_citation'] = self.cleanAndTrim(' '.join(response.xpath('//div[@id="statutory"]/p['+ str(i) + ']/text()').extract()))
        
        return program
    
    def cleanAndTrim(self, unprocessed):
        unprocessed = unprocessed.strip()
        while unprocessed.find('\n') != -1:
            if unprocessed.find('\n') > 3:
                unprocessed = unprocessed[unprocessed.find('\n')+2:]
            else:
                unprocessed = unprocessed[:unprocessed.find('\r')]
            unprocessed = unprocessed.strip()
        return unprocessed