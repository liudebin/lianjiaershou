# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
def dbHandle():
    conn = pymysql.connect(
        host = "localhost",
        user = "root",
        passwd = "liudebin-1990",
        charset = "utf8",
        use_unicode = False
    )
    return conn



class LianjiaPipeline(object):
    def process_item(self,item,spider):
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        cursor.execute("USE test")
        # sql = "INSERT INTO articles(author,title,times,url,admire,likes) VALUES(%s,%s,%s,%s,%s,%s)"
        sql = "INSERT INTO  rent_detail_lianjia(title,link,house_code," \
              "area_link,area_disc,town_link," \
              "town_disc) " \
              "VALUES(%s,%s,%s,%s,%s,%s,%s)"
        try:
            cursor.execute(sql, (item['title'], item['link'], item['house_code'],
                                 item['area_link'],
                                 item['area_disc'], item['town_link'], item['town_disc']))
            cursor.connection.commit()
        except BaseException as e:
            print("ERROR>>>>>>>>>>>>>", e, "<<<<<<<<<<<<<ERROR")
            dbObject.rollback()
        return item


# class LianjiaPipeline(object):
#     def process_item(self,item,spider):
#         dbObject = dbHandle()
#         cursor = dbObject.cursor()
#         cursor.execute("USE test")
#         # sql = "INSERT INTO articles(author,title,times,url,admire,likes) VALUES(%s,%s,%s,%s,%s,%s)"
#         sql = "INSERT INTO  lianjia_test(title,link,community_link,community,house_type," \
#               "square,direction ,con_link,con_disc,chanquan,last_price, price_update_time) " \
#               "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#         try:
#             cursor.execute(sql, (item['title'], item['link'], item['community_link'], item['community'],
#                                  item['house_type'], item['square'], item['direction'], item['con_link'],
#                                  item['con_disc'],
#                                  item['chanquan'], item['last_price'], item['price_update_time']))
#             cursor.connection.commit()
#         except BaseException as e:
#             print("ERROR>>>>>>>>>>>>>",e,"<<<<<<<<<<<<<ERROR")
#             dbObject.rollback()
#         return item

