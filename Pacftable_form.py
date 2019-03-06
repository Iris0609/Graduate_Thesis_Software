from UI.pacftable import pacftable_Form
from PyQt5.QtWidgets import *


class Pacftable_Form(QWidget, pacftable_Form):
    def __init__(self):
        super(Pacftable_Form, self).__init__()
        self.setupUi(self)



    def load(self,pacf_list):
        rows=pacf_list
        row_num=len(rows)

        if not row_num==0:
            col_num=len(rows[0])
            self.tableWidget.setColumnCount(col_num)
            self.tableWidget.setRowCount(row_num)
            VH=[]
            HH=[]
            for i in range(1,row_num+1):
                VH.append('time lag'+str(i))
            for j in range(col_num):
                HH.append('space lag' + str(j))

            self.tableWidget.setVerticalHeaderLabels(VH)
            self.tableWidget.setHorizontalHeaderLabels(HH)

            for i in range(row_num):
                for j in range(col_num):
                    temp_data = rows[i][j]  # 临时记录，不能直接插入表格
                    data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                    self.tableWidget.setItem(i, j, data)


    def show_table(self,pacflist):
        self.load(pacflist)
        if not self.isVisible():
            self.show()

    # 关闭窗口
    def close_table(self):
        self.close()