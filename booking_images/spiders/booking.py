# -*- coding: utf-8 -*-
import scrapy


class BookingSpider(scrapy.Spider):
    name = 'booking'
    allowed_domains = ['booking.com']
    start_urls = ['https://www.booking.com/hotel/br/vila-gale-cumbuco.pt-br.html']

    def parse(self, response):
        for image in response.xpath("//div[@id='photos_distinct']/a[@href]"):
            link = image.css("a ::attr(href)").extract()

            yield {'link':link}
