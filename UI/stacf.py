# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stacf.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class stacf_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(378, 377)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(40, 20, 281, 121))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_5.setObjectName("comboBox_5")
        self.horizontalLayout.addWidget(self.comboBox_5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout_2.addWidget(self.comboBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_4.setObjectName("comboBox_4")
        self.horizontalLayout_3.addWidget(self.comboBox_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 150, 301, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(35, 21, 256, 29))
        self.textEdit.setObjectName("textEdit")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(11, 21, 18, 16))
        self.label_5.setObjectName("label_5")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(40, 230, 311, 91))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_3.setObjectName("textEdit_3")
        self.horizontalLayout_5.addWidget(self.textEdit_3)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.textEdit_4 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_4.setObjectName("textEdit_4")
        self.horizontalLayout_5.addWidget(self.textEdit_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.textEdit_5 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_5.setObjectName("textEdit_5")
        self.horizontalLayout_6.addWidget(self.textEdit_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(270, 330, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "分析字段："))
        self.label.setText(_translate("Form", "时间字段："))
        self.label_6.setText(_translate("Form", "地点字段："))
        self.label_2.setText(_translate("Form", "经度："))
        self.label_3.setText(_translate("Form", "纬度："))
        self.label_4.setText(_translate("Form", "值字段："))
        self.groupBox_2.setTitle(_translate("Form", "K邻近矩阵："))
        self.label_5.setText(_translate("Form", "K："))
        self.groupBox_3.setTitle(_translate("Form", "时空自相关参数："))
        self.label_7.setText(_translate("Form", "空间滞后数："))
        self.label_8.setText(_translate("Form", "时间滞后数："))
        self.label_9.setText(_translate("Form", "平稳时空序列需要的差分计算次数："))
        self.pushButton.setText(_translate("Form", "确定"))

