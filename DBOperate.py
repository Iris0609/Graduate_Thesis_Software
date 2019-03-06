
import pymysql


class database():
    def db_execute(self,sql):
        db = pymysql.connect("localhost", "root", "960609", "biye", charset='utf8')
        #db=sqlite3.connect('/STdatabase.db')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        '''
        # 如果数据表已经存在使用 execute() 方法删除表。
        cursor.execute("DROP TABLE IF EXISTS"+"str(name)")
        # 创建数据表SQL语句
        sql = """CREATE TABLE EMPLOYEE (
                 FIRST_NAME  CHAR(20) NOT NULL,
                 LAST_NAME  CHAR(20),
                 AGE INT,  
                 SEX CHAR(1),
                 INCOME FLOAT )"""
        '''
        cursor.execute(sql)
        cursor.close()

    def db_query(self,sql):
        db = pymysql.connect("localhost", "root", "960609", "biye", charset='utf8')
        #db = sqlite3.connect('/STdatabase.db')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        cursor.close()





