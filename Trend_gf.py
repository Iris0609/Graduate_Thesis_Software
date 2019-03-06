import sys
from UI.TrendG import trendg_Form
from PyQt5.QtWidgets import *
import pymysql
from Mycanvas import *
import matplotlib.dates as mdate
from datetime import datetime


class Trendgf_Form(QWidget, trendg_Form):
    def __init__(self):
        super(Trendgf_Form, self).__init__()
        self.setupUi(self)
        self.comboBox.currentIndexChanged.connect(self.comboxchange)
        self.comboBox_4.currentIndexChanged.connect(self.combox4change)
        self.pushButton.clicked.connect(self.queren)

        global l
        l= QVBoxLayout(self.widget)
        global sc
        sc= MyStaticMplCanvas(self.widget, width=5, height=4, dpi=100)
        l.addWidget(sc)

       #self.readdb()


    #所有combo初始化
    def combo_ini(self):
        db = pymysql.connect("localhost", "root", "960609", "biye", charset='utf8')
        load_sql = "select * from AOI"
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        cursor.execute(load_sql)  # 加载表中数据
        zd = []
        for field_desc in cursor.description:
            zd.append(field_desc[0])
        self.comboBox.addItems(zd)
        self.comboBox.setCurrentIndex(0)
        self.comboBox_4.addItems(zd)
        self.comboBox_4.setCurrentIndex(0)
        self.comboBox_6.addItems(zd)
        self.comboBox_6.setCurrentIndex(0)

        field=self.comboBox.currentText()
        dt_sql="select distinct "+field+" from AOI"
        cursor.execute(dt_sql)
        rows = cursor.fetchall()
        val=[]
        for (row,) in rows:
            val_text=str(row)
            #val_text=val_text[2:-3]
            val.append(val_text)
        self.comboBox_3.addItems(val)
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_5.addItems(val)
        self.comboBox_5.setCurrentIndex(0)
        val2=val[1:]
        self.comboBox_2.addItems(val2)
        self.comboBox_2.setCurrentIndex(0)
        db.close()

    #当时间域变化
    def comboxchange(self):
        db = pymysql.connect("localhost", "root", "960609", "biye", charset='utf8')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        field=self.comboBox.currentText()
        dt_sql = "select distinct " + field + " from AOI"
        cursor.execute(dt_sql)
        rows = cursor.fetchall()
        val = []
        for (row,) in rows:
            val_text = str(row)
            #val_text = val_text[2:-3]
            val.append(val_text)
        self.comboBox_3.clear()
        self.comboBox_3.addItems(val)
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_2.clear()
        val2=val[1:]
        self.comboBox_2.addItems(val2)
        self.comboBox_2.setCurrentIndex(0)
        db.close()

    #当选择的观察个体变化
    def combox4change(self):
        db = pymysql.connect("localhost", "root", "960609", "biye", charset='utf8')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        field = self.comboBox_4.currentText()
        dt_sql = "select distinct " + field + " from AOI"
        cursor.execute(dt_sql)
        rows = cursor.fetchall()
        val = []
        for (row,) in rows:
            val_text = str(row)
            val.append(val_text)
        self.comboBox_5.clear()
        self.comboBox_5.addItems(val)
        self.comboBox_5.setCurrentIndex(0)
        db.close()

    def queren(self):
        date_field=self.comboBox.currentText()
        startdate=self.comboBox_3.currentText()
        enddate=self.comboBox_2.currentText()
        idvalue_field=self.comboBox_4.currentText()
        id_field=self.comboBox_5.currentText()
        value_field=self.comboBox_6.currentText()
        db = pymysql.connect("localhost", "root", "960609", "biye", charset='utf8')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        datetime_sql='select '+date_field+' from AOI where '+idvalue_field+'=\''+id_field+'\' and '+date_field+\
                     ' between \''+startdate+'\' and \''+enddate+'\''
        cursor.execute(datetime_sql)
        rows=cursor.fetchall()
        date_val=[]
        for (row,) in rows:
            xval=str(row)
            date_val.append(xval)
        x_val = [datetime.strptime(d, '%Y-%m-%d').date() for d in date_val]

        value_sql='select '+value_field+' from AOI where '+idvalue_field+'=\''+id_field+'\' and '+date_field+\
                     ' between \''+startdate+'\' and \''+enddate+'\''
        cursor.execute(value_sql)
        rows=cursor.fetchall()
        y_val=[]
        for (row,) in rows:
            yval=row
            y_val.append(yval)
        sc.compute_initial_figure(x_val,y_val)



    def show_form(self):
        self.combo_ini()
        if not self.isVisible():
            self.show()

        # 关闭窗口

    def close_form(self):
        self.close()


class MyStaticMplCanvas(MyMplCanvas):
    """静态画布：一条正弦线"""
    def compute_initial_figure(self,x,y):
        self.axes.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))
        self.axes.plot(x, y)
        self.draw()

    #def draw(self,x,y):
     #   self.axes.plot(x,y)

