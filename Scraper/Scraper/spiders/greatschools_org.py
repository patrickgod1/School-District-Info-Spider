# -*- coding: utf-8 -*-
import scrapy
from Scraper.items import ScraperItem
import json
import csv

class GreatschoolsOrgSpider(scrapy.Spider):
    name = 'greatschools.org'
    allowed_domains = ['greatschools.org']
    # start_urls = ['https://www.greatschools.org/schools/districts/California/CA/','https://www.greatschools.org/schools/districts/Alaska/AK/']
    with open('states.csv') as csvFile:
        start_urls = [f'https://www.greatschools.org/schools/districts/{state[0]}/{state[1]}/' for state in csv.reader(csvFile, delimiter=',')]

    # def createStateURL(self):
    #     with open('states.csv') as csvFile:
    #         return [f'https://www.greatschools.org/schools/districts/{state[0]}/{state[1]}/' for state in csv.reader(csvFile, delimiter=',')]
                 
    # def start_requests(self):
    #     urls = self.createStateURL() 
    #     for url in urls:
    #         self.outputFile = f'{url[-3:-1]}.csv'
    #         yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        # urls = response.css('td.city-district-link > a::attr(href)').extract()
        for row in response.xpath('//*[@class="table-column"]/table/tbody/tr')[1:]:
            item = ScraperItem()
            url = row.xpath('td[1]//a/@href').extract_first()
            item['Name'] = row.xpath('normalize-space(td[1]/a//text())').extract_first()
            item['City'] = row.xpath('normalize-space(td[2]//text())').extract_first()
            item['County'] = row.xpath('normalize-space(td[3]//text())').extract_first()
            yield scrapy.Request(url=f'https://www.greatschools.org{url}', callback=self.parse_details, meta={'item':item})
            # item['districtURL'] = row.xpath('td[1]//a/@href').extract_first()


        # for url in urls:
        #     yield scrapy.Request(url=f'https://www.greatschools.org{url}', callback=self.parse_details, meta={'item':item})
        # request.meta['item'] = item

    def parse_details(self, response):
        #item = ScraperItem()
        item = response.meta['item']
        data1 = json.loads(response.xpath('//script[@type="application/ld+json"]//text()').extract()[2])
        data2 = json.loads(response.xpath('//script[@type="application/json"]//text()').extract()[1])
        item['Telephone'] = data1['telephone']
        # print(data2)
        # districtURL = ''
        if "districtUrl" in data2["locality"]:
            item['DistrictURL'] = data2["locality"]["districtUrl"]
        else:
            item['DistrictURL'] = ''
        item['SchoolCount'] = data2["heroData"]["schoolCount"]
        item['Grades'] = data2["heroData"]["grades"]
        # print(telephone)
        # print(districtURL)
        # print(schoolCount)
        # print(grades)
        return item

    # def close(self):
    #     with open('AK.csv', 'a') as f:
    #         pd.DataFrame(item, columns=['Name','City','County', 'DistrictURL', 'Telephone', 'SchoolCount','Grades']).to_csv(f, sep = ',')
    # print("-----Check to see if this is closed-----")
