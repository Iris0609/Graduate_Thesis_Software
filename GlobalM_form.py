from UI.globalmoran import Gmoran_Form
from PyQt5.QtWidgets import *
import pymysql
import pysal
import numpy as np



class Globalm_Form(QWidget, Gmoran_Form):
    def __init__(self):
        super(Globalm_Form, self).__init__()
        self.setupUi(self)
        self.comboBox_4.currentIndexChanged.connect(self.combox4change)
        self.pushButton.clicked.connect(self.queren)

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
        self.comboBox_2.addItems(zd)
        self.comboBox_2.setCurrentIndex(0)
        self.comboBox_3.addItems(zd)
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_4.addItems(zd)
        self.comboBox_4.setCurrentIndex(0)

        field = self.comboBox_4.currentText()
        dt_sql = "select distinct " + field + " from AOI"
        cursor.execute(dt_sql)
        rows = cursor.fetchall()
        val = []
        for (row,) in rows:
            val_text = str(row)
            # val_text=val_text[2:-3]
            val.append(val_text)
        self.comboBox_5.addItems(val)
        self.comboBox_5.setCurrentIndex(0)
        db.close()

        # 当选择的观察个体变化

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
        K_val=self.textEdit.toPlainText()
        lon_field=self.comboBox.currentText()
        lat_field=self.comboBox_2.currentText()
        time_field=self.comboBox_4.currentText()
        time_val=self.comboBox_5.currentText()
        val_field=self.comboBox_3.currentText()

        db = pymysql.connect("localhost", "root", "960609", "biye", charset='utf8')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        #datetime_sql='select '+date_field+' from AOI where '+idvalue_field+'=\''+id_field+'\' and '+date_field+\
         #            ' between '+startdate+' and '+enddate
        #点的经度
        lon_sql='select '+lon_field+' from AOI where '+time_field+'=\''+time_val+'\''
        cursor.execute(lon_sql)
        rows=cursor.fetchall()
        x_val=[]
        for (row,) in rows:
            xval=row
            x_val.append(xval)

        #点的纬度
        lat_sql = 'select ' + lat_field + ' from AOI where ' + time_field + '=\''+ time_val+'\''
        cursor.execute(lat_sql)
        rows=cursor.fetchall()
        y_val=[]
        for (row,) in rows:
            yval=row
            y_val.append(yval)

        point=[]
        for i in range(len(x_val)):
            #coor='('+str(x_val[i])+','+str(y_val[i])+')'
            coor=[]
            coor.append(x_val[i])
            coor.append(y_val[i])
            coortuple=tuple(coor)
            point.append(coortuple)

        #计算moran值
        val_sql= 'select ' + val_field + ' from AOI where ' + time_field + '=\''+ time_val+'\''
        cursor.execute(val_sql)
        rows = cursor.fetchall()
        val = []
        for (row,) in rows:
            v_val = row
            val.append(v_val)
        self.cal_moran(point,val,K_val)


    def cal_moran(self,coors,value,K):
        kd = pysal.cg.kdtree.KDTree(np.array(coors))
        # wnn2 = pysal.KNN(kd, 2)
        # weights
        K=int(K)
        weights = pysal.weights.Distance.KNN(kd, K)
        # moran i
        moran_i = pysal.Moran(value, weights, two_tailed=False)
        moran_index=moran_i.I
        expect_index=moran_i.EI
        variance_val=moran_i.VI_norm
        z_score=moran_i.z_norm
        z_=moran_i.z_sim
        p=moran_i.p_sim
        p_val=moran_i.p_norm
        self.textBrowser.setText('Global Moran\'s I Summary')
        self.textBrowser.append('Moran\'s Index: '+str(moran_index))
        #self.textBrowser.append('z-score: ' + str(z_score))
        self.textBrowser.append('p-value: ' + str(p_val))

    def show_form(self):
        self.combo_ini()
        if not self.isVisible():
            self.show()

        # 关闭窗口

    def close_form(self):
        self.close()