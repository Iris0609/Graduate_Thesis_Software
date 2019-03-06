import sys
from UI.Timelinemap import timelinemap_Form
from PyQt5.QtWidgets import *
import pymysql
from pyecharts import Geo
from pyecharts import Timeline
from Webviewer import Dynamicmap


class Timeline_Form(QWidget, timelinemap_Form):
    def __init__(self):
        super(Timeline_Form, self).__init__()
        self.setupUi(self)
        self.comboBox.currentIndexChanged.connect(self.comboxchange)
        #self.comboBox_4.currentIndexChanged.connect(self.combox4change)
        self.pushButton.clicked.connect(self.queren)
        self.dywebmap=Dynamicmap()

        # 所有combo初始化

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
        self.comboBox_8.addItems(zd)
        self.comboBox_8.setCurrentIndex(0)
        # 起始时间终止时间初始化
        field = self.comboBox.currentText()
        dt_sql = "select distinct " + field + " from AOI"
        cursor.execute(dt_sql)
        rows = cursor.fetchall()
        val = []
        for (row,) in rows:
            val_text = str(row)
            # val_text=val_text[2:-3]
            val.append(val_text)
        self.comboBox_3.addItems(val)
        self.comboBox_3.setCurrentIndex(0)
        global spacename
        spacename= ['world','china','北京','安徽','澳门','重庆','福建','甘肃','广东','广西','海南','河北','黑龙江',
                          '河南','湖北','湖南','江苏','江西','吉林','辽宁','内蒙古','宁夏','青海','山东','上海','陕西',
                          '山西','四川','台湾','天津','香港','新疆','西藏','云南','浙江']
        self.comboBox_6.addItems(spacename)
        self.comboBox_6.setCurrentIndex(0)
        val2 = val[1:]
        self.comboBox_2.addItems(val2)
        self.comboBox_2.setCurrentIndex(0)
        db.close()
        map_type=['scatter', 'effectScatter', 'heatmap']
        self.comboBox_7.addItems(map_type)
        self.comboBox_7.setCurrentIndex(0)

        # 当时间域变化
    def comboxchange(self):
        db = pymysql.connect("localhost", "root", "960609", "biye", charset='utf8')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        field = self.comboBox.currentText()
        dt_sql = "select distinct " + field + " from AOI"
        cursor.execute(dt_sql)
        rows = cursor.fetchall()
        val = []
        for (row,) in rows:
            val_text = str(row)
            # val_text = val_text[2:-3]
            val.append(val_text)
        self.comboBox_3.clear()
        self.comboBox_3.addItems(val)
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_2.clear()
        val2 = val[1:]
        self.comboBox_2.addItems(val2)
        self.comboBox_2.setCurrentIndex(0)
        db.close()

    def queren(self):
        date_field=self.comboBox.currentText()
        startdate=self.comboBox_3.currentText()
        enddate=self.comboBox_2.currentText()
        spacefield=self.comboBox_4.currentText()
        space_val=self.comboBox_6.currentText()
        maptype_val=self.comboBox_7.currentText()
        aoi_val=self.comboBox_8.currentText()
        db = pymysql.connect("localhost", "root", "960609", "biye", charset='utf8')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        #找对应的时间
        if space_val=='china' or space_val=='world':
            datetime_sql='select distinct '+ date_field+' from AOI where '+date_field+\
                     ' between \''+startdate+'\' and \''+enddate+'\''
        else:
            #这里字段写死了，表中一定要有province字段
            datetime_sql='select distinct '+ date_field+' from AOI where province'+'=\''+space_val+'\' and '+date_field+\
                     ' between \''+startdate+'\' and \''+enddate+'\''
        cursor.execute(datetime_sql)
        rows=cursor.fetchall()
        time_val=[]
        for (row,) in rows:
            timeval=str(row)
            time_val.append(timeval)

        # 加入时间轴
        timeline = Timeline()
        #单张地图
        for i in range(len(time_val)):
            # 查找地名
            if space_val == 'china' or space_val == 'world':
                location_sql = 'select ' + spacefield + ' from AOI where ' + date_field + '=\'' + time_val[i]+'\''
            else:
                location_sql = 'select ' + spacefield + ' from AOI where province =\'' + space_val + '\' and ' + date_field + \
                               '=\'' + time_val[i]+'\''
            cursor.execute(location_sql)
            rows = cursor.fetchall()
            location_val = []
            for (row,) in rows:
                locationval = str(row)
                location_val.append(locationval)

            # 查找值
            if space_val == 'china' or space_val == 'world':
                value_sql = 'select ' + aoi_val + ' from AOI where ' + date_field + '=\'' + time_val[i]+'\''
            else:
                value_sql = 'select ' + aoi_val + ' from AOI where province'+ '=\'' + space_val + '\' and ' + date_field + \
                            '=\'' + time_val[i]+'\''
            cursor.execute(value_sql)
            rows = cursor.fetchall()
            val = []
            for (row,) in rows:
                aoival = str(row)
                val.append(aoival)


            # 设置一张地图
            geo = Geo("", width=1000, height=600, background_color='#404a59')
            self.drawtimeline(location_val, val, geo, space_val, maptype_val)
            timeline.add(geo, str(time_val[i]))
        timeline.render("test.html")
        self.dywebmap.show_table()



    def show_form(self):
        self.combo_ini()
        if not self.isVisible():
            self.show()

            # 关闭窗口

    def close_form(self):
        self.close()


    def drawtimeline(self,location,value,geo,space,maptype):
        data=[]
        for i in range(len(value)):
            eachdata = []
            eachdata.append(location[i])
            eachdata.append(value[i])
            mapdata = tuple(eachdata)
            data.append(mapdata)
        # 设置一张地图
        attr, value = geo.cast(data)
        geo.add("", attr, value,type=maptype, visual_range=[0, 500], maptype=space, visual_text_color="#fff",
                symbol_size=10, is_visualmap=True)














