# coding: utf-8

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
#from UI.webmap import Webmap_Form


class Dynamicmap(QWidget):
    '''
    def __init__(self):
        super(Dynamicmap, self).__init__()
        self.setupUi(self)
        self.widget=QWebEngineView()

        self.setWindowTitle("Map")
        self.resize(900, 600)

        #self.browser = QWebEngineView()
        #self.show()
        #self.setCentralWidget(self.browser)

    def show_table(self):
        if not self.isVisible():
            #url = 'https://www.baidu.com'
            url='http://localhost:63342/software/test.html'
            self.widget.load(QUrl(url))
    '''

    def __init__(self, parent=None):
        super(Dynamicmap, self).__init__(parent)

        # self.setWindowOpacity(1)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        # self.showFullScreen()
        rect = QApplication.desktop().screenGeometry()
        self.resize(rect.width(), rect.height())
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        self.webview = QWebEngineView()

        vbox = QVBoxLayout()
        vbox.addWidget(self.webview)
        self.resize(900,600)



        # self.setWindowTitle("CoDataHD")
        # webview.load(QUrl('http://www.cnblogs.com/misoag/archive/2013/01/09/2853515.html'))
        # webview.show()

    def show_table(self):
        url='http://localhost:63342/software/test.html'
        self.webview.load(QUrl(url))
        #self.show()
        self.webview.show()







