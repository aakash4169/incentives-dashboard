# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class TestItem(Item):
    numRecords = Field()

class ProgramItem(Item):
    program_name = Field()
    department = Field()
    state = Field()
    program_category = Field()
    program_type = Field()
    business_needs = Field()
    program_industries = Field()
    geographic_focus = Field()
    website = Field()
    additional_website = Field()
    contact_address = Field()
    contact_info = Field()
    contact_email = Field()
    program_description = Field()
    program_objectives = Field()
    program_specifics = Field()
    eligibility_requirements = Field()
    application_information = Field()
    program_start = Field()
    program_finish = Field()
    program_cap = Field()
    program_administration_type = Field()
    legal_citation = Field()