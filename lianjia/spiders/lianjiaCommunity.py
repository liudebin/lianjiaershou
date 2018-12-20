# coding=utf-8
import scrapy

from msysqlDb import mysqlHadler

baseUrl = 'https://sh.lianjia.com'


def getList(a):
    print a
    if a:
        if a[0].extract().isdigit():
            return a[0].extract()
        return a[0].extract().strip()
    else:
        return ""


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'lianjiaCommunity'

    # box = []
    # for num in range(102):
    #     pages = 'https://sh.lianjia.com/zufang/pudong/pg{0}/#contentList'.format(num)
    #     box.append(pages)
    # start_urls = box

    # start_urls = [
    #     'https://sh.lianjia.com/zufang/pudong',
    # ]

    dbObject = mysqlHadler().dbHandle()
    cursor = dbObject.cursor()
    cursor.execute("USE test")
    # sql = "INSERT INTO articles(author,title,times,url,admire,likes) VALUES(%s,%s,%s,%s,%s,%s)"
    sql = "select distinct community_link link from rent_detail_lianjia where community_code is not null ;"
    cursor.execute(sql)
    results = cursor.fetchall()
    box = []
    for row in results:
        box.append(row[0])
    start_urls = box

    def parse(self, response):
        print response
        for quote in response.xpath('//div[@class="content__list--item"]'):
            # print quote
            price = int(quote.xpath('.//span[@class="content__list--item-price"]/em/text()')[0].extract())
            yield {
                'title': getList(quote.xpath('.//div/p[@class="content__list--item--title twoline"]/a/text()')),
                'link': baseUrl + getList(quote.xpath('.//div/p[@class="content__list--item--title twoline"]/a/@href')),
                'house_code': getList(quote.xpath('.//div/p[@class="content__list--item--title twoline"]/a/@href'))[8:-5],
                'area_link': baseUrl + getList(quote.xpath('.//div/p[@class="content__list--item--des"]/a[position()=1]/@href')),
                'area_disc': getList(
                    quote.xpath('.//div/p[@class="content__list--item--des"]/a[position()=1]/text()')),
                'town_link': baseUrl + getList(
                    quote.xpath('.//div/p[@class="content__list--item--des"]/a[position()=2]/@href')),
                'town_disc': getList(
                    quote.xpath('.//div/p[@class="content__list--item--des"]/a[position()=2]/text()')),
                'price': price
            }

            # next_page_url = response.css("li.next > a::attr(href)").extract_first()
            # if next_page_url is not None:
            #     yield scrapy.Request(response.urljoin(next_page_url))
