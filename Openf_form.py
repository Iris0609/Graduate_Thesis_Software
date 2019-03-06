from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from UI.testui import Ui_MainWindow
from UI.openfile import Ui_Form
import csv
from DBOperate import database as db
from Table_form import *




class Openf_Form(QWidget, Ui_Form):
    #table = Table_form()
    def __init__(self):
        super(Openf_Form, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.openMsg)
        self.pushButton_2.clicked.connect(self.queren)
        self.table=Table_Form()

    #打开文件
    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, "打开", "F:/biyedata", "All Files (*);;Text Files (*.txt)")
        self.textEdit.setText(file)
        #self.Tableview_init(file)
        self.Tablewidget_init(file)

    def Tablewidget_init(self,file=""):
        # set combo box choices:
        choices = ['int', 'double', 'float', 'decimal', 'char', 'varchar(255)', 'date', 'time', 'datetime', 'text']
        num=0
        combo=QComboBox()
        combo.addItems(choices)
        combo.setCurrentIndex(0)
        self.tableWidget.setColumnCount(2)
        horizontalHeader = ["name","type"]
        self.tableWidget.setHorizontalHeaderLabels(horizontalHeader)
        # 当还未打开文件
        if file == "":
            self.tableWidget.setCellWidget(0,1,combo)
        # 打开文件后
        else:
            # 读取文件
            with open(file)as file_data:
                reader = csv.DictReader(file_data)
                for i, rows in enumerate(reader):
                    if i == 0:
                        row = rows
                self.tableWidget.setRowCount(len(row))
                for item in row:
                    combo = QComboBox()
                    combo.addItems(choices)
                    combo.setCurrentIndex(0)
                    self.tableWidget.setItem(num,0,QTableWidgetItem(item))
                    self.tableWidget.setCellWidget(num, 1, combo)
                    num=num+1

    def queren(self):
        file = self.textEdit.toPlainText()
        database = db()
        #db=sqlite3.connect('/STdatabase.db')
        #检查表是否存在
        check_sql = 'DROP TABLE IF EXISTS AOI'
        database.db_execute(check_sql)
        #db.execute(check_sql)
        field = ''
        row_num=self.tableWidget.rowCount()
        #获取表字段
        for i in range(row_num):
            name=self.tableWidget.item(i,0).text()
            type=self.tableWidget.cellWidget(i,1).currentText()
            field = field + name + ' ' + type + ','
        field = field[:-1]
        #创建表
        create_sql = 'create table AOI (' + field + ')'
        database.db_execute(create_sql)
        #db.execute(check_sql)
        #向表中添加字段
        #insert_data = pandas.read_csv(file, encoding='gbk', header=1, sep=',')
        #insert_data.to_sql('aoi',db,if_exists='append',index=False)
        insert_sql = 'LOAD DATA INFILE \'' + file + '\' INTO TABLE AOI character set gbk FIELDS TERMINATED BY \',\' ENCLOSED BY \'\"\' LINES TERMINATED BY \'' + r'\r\n' + '\' IGNORE 1 LINES;'
        database.db_query(insert_sql)
        self.table.show_table()



    def show_fileopen(self):
        if not self.isVisible():
            self.show()
        self.Tablewidget_init()

    # 关闭窗口
    def close_fileopen(self):
        self.close()



