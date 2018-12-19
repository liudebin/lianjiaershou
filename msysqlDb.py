import pymysql


class mysqlHadler:
    def dbHandle(self):
        conn = pymysql.connect(
            host="localhost",
            user="root",
            passwd="liudebin-1990",
            charset="utf8",
            use_unicode=False
        )
        return conn
