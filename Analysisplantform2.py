# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Analysisplantform.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(739, 450)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(290, 30, 131, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 80, 321, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pic1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.pic1.setObjectName("pic1")
        self.horizontalLayout.addWidget(self.pic1)
        self.color1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.color1.setObjectName("color1")
        self.horizontalLayout.addWidget(self.color1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(70, 220, 321, 111))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pic2_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.pic2_2.setObjectName("pic2_2")
        self.horizontalLayout_2.addWidget(self.pic2_2)
        self.color2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.color2.setObjectName("color2")
        self.horizontalLayout_2.addWidget(self.color2)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(80, 200, 54, 12))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(300, 200, 81, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(80, 340, 54, 12))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(300, 340, 81, 16))
        self.label_9.setObjectName("label_9")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(600, 360, 41, 21))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(440, 80, 251, 251))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "竞品分析平台"))
        self.pic1.setText(_translate("Dialog", "TextLabel"))
        self.color1.setText(_translate("Dialog", "TextLabel"))
        self.pic2_2.setText(_translate("Dialog", "TextLabel"))
        self.color2.setText(_translate("Dialog", "TextLabel"))
        self.label_6.setText(_translate("Dialog", "商品1名称"))
        self.label_7.setText(_translate("Dialog", "颜色分布图"))
        self.label_8.setText(_translate("Dialog", "商品2名称"))
        self.label_9.setText(_translate("Dialog", "颜色分布图"))
        self.label_2.setText(_translate("Dialog", "logo"))
