from UI.localmoran import Lmoran_Form
from PyQt5.QtWidgets import *
import pymysql
import pysal
import numpy as np
from Mycanvas import *



class Localm_Form(QWidget, Lmoran_Form):
    def __init__(self):
        super(Localm_Form, self).__init__()
        self.setupUi(self)
        self.comboBox_4.currentIndexChanged.connect(self.combox4change)
        self.pushButton.clicked.connect(self.queren)

        global l
        l = QVBoxLayout(self.widget)
        global sc
        sc = MyStaticMplCanvas(self.widget, width=5, height=4, dpi=100)
        l.addWidget(sc)

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
        lat_sql = 'select ' + lat_field + ' from AOI where ' + time_field + '=\'' + time_val+'\''
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
        self.cal_localmoran(point,val,K_val)

    def cal_localmoran(self,coors,value,K):
        kd = pysal.cg.kdtree.KDTree(np.array(coors))
        # wnn2 = pysal.KNN(kd, 2)
        # weights
        K=int(K)
        weights = pysal.weights.Distance.KNN(kd, K)
        #local moran
        localm=pysal.Moran_Local(value,weights)
        std_val = np.std(value,ddof=1)
        avg_val = np.average(value)
        x_val=[]    #标准化的观测值
        for i in range(len(value)):
            guance_val=(value[i]-avg_val)/std_val
            x_val.append(guance_val)
        #neighbors
        neib=weights.neighbors
        y_val = []
        for i in range(len(neib)):
            kneib=neib[i]
            kval=0
            for j in kneib:
                kval=kval+x_val[j]/K
            y_val.append(kval)

        sc.compute_initial_figure(x_val, y_val)



    def show_form(self):
        self.combo_ini()
        if not self.isVisible():
            self.show()

        # 关闭窗口

    def close_form(self):
        self.close()

class MyStaticMplCanvas(MyMplCanvas):
    """静态画布：一条正弦线"""

    def compute_initial_figure(self, x, y):
        self.axes.scatter(x, y,marker='o')
        # 移位置 设为原点相交
        self.axes.xaxis.set_ticks_position('bottom')
        self.axes.spines['bottom'].set_position(('data', 0))
        self.axes.yaxis.set_ticks_position('left')
        self.axes.spines['left'].set_position(('data', 0))
        self.axes.set_xlabel('STD')
        self.axes.set_ylabel('LAG')
        self.axes.set_title('Local Moran\'s I')
        for i in range(len(x)):
            self.axes.annotate(i,xy=(x[i],y[i]))
        self.draw()

        ##可以把标注改成具体的id


