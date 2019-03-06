import sys
from UI.table import table_Form
from PyQt5.QtWidgets import *
import pymysql
import sqlite3


class Table_Form(QWidget, table_Form):
    def __init__(self):
        super(Table_Form, self).__init__()
        self.setupUi(self)


    def load(self):
        db = pymysql.connect("localhost", "root", "960609", "biye", charset='utf8')
        #db=sqlite3.connect('/STdatabase.db')
        #check_sql="create table AOI if not exists \'AOI\'"
        load_sql="select * from AOI"
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # 获取表的列名
        #cursor.execute("SELECT * FROM {}".format('aoi'))
        #col_name_list = [tuple[0] for tuple in cursor.description]
        #self.tableWidget.setHorizontalHeaderLabels(col_name_list)

        #cursor.execute(check_sql)#判断表是否存在
        cursor.execute(load_sql)#加载表中数据
        zd=[]
        for field_desc in cursor.description:
            zd.append(field_desc[0])
        self.tableWidget.setHorizontalHeaderLabels(zd)
        rows=cursor.fetchall()
        row_num=cursor.rowcount

        if not row_num==0:
            col_num=len(rows[0])
            cursor.close()
            db.close()
            self.tableWidget.setColumnCount(col_num)
            self.tableWidget.setRowCount(row_num)

            for i in range(row_num):
                for j in range(col_num):
                    temp_data = rows[i][j]  # 临时记录，不能直接插入表格
                    data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                    self.tableWidget.setItem(i, j, data)


    def show_table(self):
        self.load()
        if not self.isVisible():
            self.show()

    # 关闭窗口
    def close_table(self):
        self.close()