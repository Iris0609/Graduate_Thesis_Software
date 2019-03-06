import sys
from UI.stpacf import stpacf_Form
from PyQt5.QtWidgets import *
import pymysql
from datetime import datetime
import numpy as np
from pySTARMA import stacf_stpacf,starma_model,utils
import pysal
from Pacftable_form import *

class Stpacf_Form(QWidget, stpacf_Form):
    def __init__(self):
        super(Stpacf_Form, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.queren)
        self.table = Pacftable_Form()

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
        self.comboBox_5.addItems(zd)
        self.comboBox_5.setCurrentIndex(0)
        db.close()

    def queren(self):
        time_field = self.comboBox.currentText()
        lon_field = self.comboBox_2.currentText()
        lat_field = self.comboBox_3.currentText()
        val_field = self.comboBox_4.currentText()
        location_field = self.comboBox_5.currentText()
        K_val = int(self.textEdit.toPlainText())
        s_lag = int(self.textEdit_3.toPlainText())
        t_lag = int(self.textEdit_4.toPlainText())
        diff_val = int(self.textEdit_5.toPlainText())

        db = pymysql.connect("localhost", "root", "960609", "biye", charset='utf8')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 获取地点字段
        location_sql = 'select distinct ' + location_field + ' from AOI'
        cursor.execute(location_sql)
        rows = cursor.fetchall()
        location_val = []
        for (row,) in rows:
            loca = row
            location_val.append(loca)

        # 获取时间字段
        time_sql = 'select distinct ' + time_field + ' from AOI'
        cursor.execute(time_sql)
        rows = cursor.fetchall()
        datetime_val = []
        for (row,) in rows:
            dt = str(row)
            datetime_val.append(dt)

        data = []
        diff = [diff_val]  # 差分次数i
        # 拼接时空数据
        for i in range(len(datetime_val)):
            locaval_sql = 'select ' + val_field + ' from AOI where ' + time_field + ' = \'' + datetime_val[i
            ] + '\' order by ' + location_field + ' asc'
            cursor.execute(locaval_sql)
            rows = cursor.fetchall()
            lval = []
            for (row,) in rows:
                val = row
                lval.append(val)
            data.append(lval)
        ts = np.array(data)
        # 计算差分
        ts_diff = utils.set_stationary(ts, diff)
        # 获取点的经纬度坐标
        # 点的经度
        lon_sql = 'select distinct ' + lon_field + ' from AOI order by ' + location_field + ' asc'
        cursor.execute(lon_sql)
        rows = cursor.fetchall()
        x_val = []
        for (row,) in rows:
            xval = row
            x_val.append(xval)

        # 点的纬度
        lat_sql = 'select distinct ' + lat_field + ' from AOI order by ' + location_field + ' asc'
        cursor.execute(lat_sql)
        rows = cursor.fetchall()
        y_val = []
        for (row,) in rows:
            yval = row
            y_val.append(yval)

        # 拼接点
        point = []
        for i in range(len(x_val)):
            coor = []
            coor.append(x_val[i])
            coor.append(y_val[i])
            coortuple = tuple(coor)
            point.append(coortuple)
        # 计算权重
        points = np.array(point)
        kd = pysal.cg.kdtree.KDTree(points)
        # weights
        K = int(K_val)
        weights = pysal.weights.Distance.KNN(kd, K)
        # weights.transform='r'
        # 计算滞后
        w0 = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        ]
        w = [weights]
        for s in range(2, s_lag + 1):
            w_tmp = pysal.higher_order(weights, s)
            w.append(w_tmp)

        slw = [w0]
        for j in range(len(w)):
            w[j].transform = 'r'
            w_f = w[j].full()
            slw.append(w_f[0].tolist())

        w_slag = np.array(slw)
        pacf = stacf_stpacf.Stpacf(ts_diff, w_slag, t_lag)
        pacf_val = pacf.estimate()
        # print(acf_val)
        self.table.show_table(pacf_val)

    def show_form(self):
        self.combo_ini()
        if not self.isVisible():
            self.show()

            # 关闭窗口

    def close_form(self):
        self.close()
