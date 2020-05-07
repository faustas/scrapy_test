# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import csv
import os
from selectorlib import Extractor
import re

class HeiseCrawlerSpider(scrapy.Spider):
    name = 'heise_crawler'
    allowed_domains = ['heise.de']
    start_urls = ['https://www.heise.de/']
    extractor = Extractor.from_yaml_file(os.path.join(os.path.dirname(__file__), "../resources/heise_selectors.yml"))
    max_pages = 5

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = self.extractor.extract(response.text, base_url=response.url)
        for article in data['articles']:
            yield article
