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
origin_url = "http://www.zimuku.net/search?q=&t=onlyst&ad=1&p=%d"


class SubTitleSpider(scrapy.Spider):
    name = "subtitle"
    # 减慢爬取速度 为1s
    download_delay = 1

    allowed_domains = ["zimuku.net"]
    start_urls = []

    for index in xrange(1, 3):
        next_url = origin_url % index
        start_urls.append(next_url)

    def parse(self, response):
        # logger.info('Parse url: %s' % response.url)
        hrefs = response.selector.xpath('//div[contains(@class, "persub")]/h1/a/@href').extract()

        for href in hrefs:
            url = response.urljoin(href)
            request = scrapy.Request(url, callback=self.parse_detail)
            yield request

    def parse_detail(self, response):
        url = response.selector.xpath('//li[contains(@class, "dlsub")]/div/a/@href').extract()[0]
        code, msg = commands.getstatusoutput('wget -q --tries=3 --directory-prefix=result/ %s' % (url))

        if code != 0:
            logger.info(msg)
            print url
        # request = scrapy.Request(url, callback=self.parse_file)
        # yield request

    def parse_file(self, response):
        filename = re.findall(r'attachment; filename="(.*)"', response.headers.get('Content-Disposition', ''))
        body = response.body
        item = SubtitleCrawlerItem()
        item['url'] = response.url
        item['body'] = body
        item['filename'] = filename
        return item
