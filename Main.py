from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from UI.testui import Ui_MainWindow
from Openf_form import Openf_Form
from Table_form import Table_Form
from Trend_gf import Trendgf_Form
from GlobalM_form import Globalm_Form
from LocalMform import Localm_Form
from Timemap_form import Timeline_Form
from STacf_Form import Stacf_Form
from STpaf_Form import Stpacf_Form
from STARMA_Form import Starma_Form

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        #self.actionOpen.triggered.connect(Openf_Form.show_fileopen)  # 打开别的窗口不可以再这里加，因为别的窗口没有初始化


    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, "打开", "C:/", "CSV (*.csv)")
        self.statusbar.showMessage(file)  # 在状态栏显示文件地址


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    openf=Openf_Form()
    tablef=Table_Form()
    Trendg=Trendgf_Form()
    gmoran=Globalm_Form()
    lmoran=Localm_Form()
    timelinemap=Timeline_Form()
    stacf=Stacf_Form()
    stpacf=Stpacf_Form()
    starma=Starma_Form()

    myshow.actionOpen.triggered.connect(openf.show_fileopen)
    myshow.actionTable.triggered.connect(tablef.show_table)
    myshow.actionTrend_Graph.triggered.connect(Trendg.show_form)
    myshow.actionGlobal.triggered.connect(gmoran.show_form)
    myshow.actionLocal.triggered.connect(lmoran.show_form)
    myshow.actionDynamic_Map.triggered.connect(timelinemap.show_form)
    myshow.actionSTACF.triggered.connect(stacf.show_form)
    myshow.actionSTPACF.triggered.connect(stpacf.show_form)
    myshow.actionSTARMA.triggered.connect(starma.show_form)
    myshow.show()
    sys.exit(app.exec_())