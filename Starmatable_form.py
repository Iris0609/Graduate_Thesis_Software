from UI.starmatable import starmatable_Form
from PyQt5.QtWidgets import *


class STarmatable_Form(QWidget, starmatable_Form):
    def __init__(self):
        super(STarmatable_Form, self).__init__()
        self.setupUi(self)



    def load(self,starma_list,location):
        rows=starma_list
        row_num=len(rows)

        if not row_num==0:
            col_num=len(rows[0])
            self.tableWidget.setColumnCount(col_num)
            self.tableWidget.setRowCount(row_num)
            HH=location

            self.tableWidget.setHorizontalHeaderLabels(HH)

            for i in range(row_num):
                for j in range(col_num):
                    temp_data = rows[i][j]  # 临时记录，不能直接插入表格
                    data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                    self.tableWidget.setItem(i, j, data)


    def show_table(self,starmalist,location):
        self.load(starmalist,location)
        if not self.isVisible():
            self.show()

    # 关闭窗口
    def close_table(self):
        self.close()