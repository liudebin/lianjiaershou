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
    name = 'lianjiaTown'

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
    sql = "select distinct pinyin link from lianjia_town ";
    cursor.execute(sql)
    results = cursor.fetchall()
    box = []
    for row in results:
        for num in 50:
            box.append("https://sh.lianjia.com/ershoufang/" + row[0]+"/pg{0}".format(num))
    start_urls = box

    def parse(self, response):
        for quote in response.xpath('//li [@class="clear LOGCLICKDATA"]'):
            title = getList(quote.xpath('.//div[@class="info clear"]/div[@class="title"]/a/text()'))
            link = getList(quote.xpath('.//a[@class="noresultRecommend img "]/@href'))
            house_code = getList(quote.xpath('.//a[@class="noresultRecommend img "]/@data-housecode'))
            community_code = getList(quote.xpath(
                './/div[@class="info clear"]/div[@class="priceInfo"]/div[@class="unitPrice"]/@data-rid'))

            community_link = getList(
                quote.xpath('.//div[@class="info clear"]/div[@class="address"]/div[@class="houseInfo"]/a/@href'))
            community = getList(
                quote.xpath('.//div[@class="info clear"]/div[@class="address"]/div[@class="houseInfo"]/a/text()'))

            town_link = getList(
                quote.xpath('.//div[@class="info clear"]/div[@class="flood"]/div[@class="positionInfo"]/a/@href'))
            town_disc = getList(
                quote.xpath('.//div[@class="info clear"]/div[@class="flood"]/div[@class="positionInfo"]/a/text()'))

            nn = quote.xpath('.//div[@class="info clear"]/div[@class="address"]/div[@class="houseInfo"]')
            house_info = nn[0].xpath('string(.)')[0].extract().replace("\n", "").replace("  ", "")
            chan_quan = quote.xpath('.//div[@class="info clear"]/div[@class="flood"]/div[@class="positionInfo"]')[0] \
                            .xpath('string(.)')[0].extract().replace("\n", "").replace("  ", ""),

            follow_info = quote.xpath('.//div[@class="info clear"]/div[@class="followInfo"]')[0].xpath(
                'string(.)')[0].extract() \
                .replace("\n", "").replace("  ", "")
            tags = quote.xpath('.//div[@class="info clear"]/div[@class="tag"]')[0].xpath('string(.)')[0].extract() \
                .replace("\n", "").replace("  ", "")
            price = int(
                quote.xpath('.//div[@class="info clear"]/div[@class="priceInfo"]/div[@class="totalPrice"]/span/text()')[
                    0].extract())
            price_content = quote.xpath('.//div[@class="info clear"]/div[@class="priceInfo"]/div[@class="totalPrice"]')[
                0] \
                .xpath('string(.)')[0].extract().replace("\n", "").replace("  ", "")
            unit_price = getList(
                quote.xpath('.//div[@class="info clear"]/div[@class="priceInfo"]/div[@class="unitPrice"]/span/text()'))

            yield {
                'title': title,
                'link': link,
                'house_code': house_code,
                'community_code': community_code,

                'community_link': community_link,
                'community': community,
                'town_link': town_link,
                'town_disc': town_disc,
                'house_info': house_info,
                'chan_quan':
                    chan_quan,
                'follow_info': follow_info,
                'tags': tags,
                'price': price,
                'price_content': price_content,
                'unit_price': unit_price
            }

            # next_page_url = response.css("li.next > a::attr(href)").extract_first()
            # if next_page_url is not None:
            #     yield scrapy.Request(response.urljoin(next_page_url))
