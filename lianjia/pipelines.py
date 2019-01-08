# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from msysqlDb import mysqlHadler


class LianjiaPipeline(object):
    def process_item(self,item,spider):
        dbObject = mysqlHadler().dbHandle()
        cursor = dbObject.cursor()
        cursor.execute("USE test")
        # sql = "INSERT INTO articles(author,title,times,url,admire,likes) VALUES(%s,%s,%s,%s,%s,%s)"
        sql = "INSERT INTO  ershoufang_detail_lianjia(title,link,house_code," \
              "community_code,community_link,community,town_link," \
              "town_disc, info,chan_quan,follow_info,tags,price,price_content," \
              "uni_price_content, rent_status) " \
              "VALUES(%s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s, 0)" \
              " on duplicate key update rent_status = 2 "
        # sql1 = "insert rent_scrapy_tmp(house_code) values(%s) "
        try:
            cursor.execute(sql, (item['title'], item['link'], item['house_code'],
                                 item['community_code'],
                                 item['community_link'],
                                 item['community'],
                                 item['town_link'],
                                 item['town_disc'],
                                 item['house_info'],
                                 item['chan_quan'],
                                 item['follow_info'],
                                 item['tags'],
                                 item['price'],
                                 item['price_content'], item['unit_price']))
            cursor.connection.commit()
        except BaseException as e:
            print("ERROR>>>>>>>>>>>>>", e, "<<<<<<<<<<<<<ERROR")
            dbObject.rollback()

        # cursor.execute(sql1, item['house_code'])
        # cursor.connection.commit()
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

