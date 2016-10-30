# coding:utf-8

import sys
import re
import logging
import commands

import scrapy
from subtitle_crawler.items import SubtitleCrawlerItem


reload(sys)
sys.setdefaultencoding("utf-8")

logger = logging.getLogger('SubTitleSpider')
origin_url = "http://www.zimuku.net/search?q=&ad=1&p=%d"


class SubTitleSpider(scrapy.Spider):
    name = "subtitle"
    # 减慢爬取速度 为1s
    download_delay = 1

    allowed_domains = ["zimuku.net"]
    start_urls = []

    for index in xrange(1, 1772):
        next_url = origin_url % index
        start_urls.append(next_url)

    def parse(self, response):
        hrefs = response.selector.xpath('//div[contains(@class, "prel")]/div[contains(@class, "title")]/p/a/@href').extract()

        for href in hrefs:
            url = response.urljoin(href)
            request = scrapy.Request(url, callback=self.parse_subs)
            yield request

    def parse_subs(self, response):
        hrefs = response.selector.xpath('//table[contains(@id, "subtb")]/tbody/tr/td[contains(@class, "first")]/a/@href').extract()

        for href in hrefs:
            url = response.urljoin(href)
            request = scrapy.Request(url, callback=self.parse_detail)
            yield request

    def parse_detail(self, response):
        file_name = response.selector.xpath('//h1/@title').extract()[0]
        url = response.selector.xpath('//div[contains(@class, "clearfix")]/a/@href').extract()[0]
        url_download = 'http://www.zimuku.net' + url

        code, msg = commands.getstatusoutput('wget -q --restrict-file-names=nocontrol --tries=3 -O \'result/%s\' %s' % (file_name, url_download))

        if code != 0:
            logger.info(msg)
            print url

    def parse_file(self, response):
        filename = re.findall(r'attachment; filename="(.*)"', response.headers.get('Content-Disposition', ''))
        body = response.body
        item = SubtitleCrawlerItem()
        item['url'] = response.url
        item['body'] = body
        item['filename'] = filename
        return item
