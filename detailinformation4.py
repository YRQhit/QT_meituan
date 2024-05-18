# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detailinformation.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import time

class detailinformation_Dialog(object):
    def __init__(self, product_id1, product_id2):
        self.product_id1 = product_id1
        self.product_id2 = product_id2
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(414, 435)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 20, 81, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 210, 291, 127))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.itemid2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.itemid2.setObjectName("itemid2")
        self.gridLayout.addWidget(self.itemid2, 2, 3, 1, 1)
        self.itemname2 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.itemname2.setObjectName("itemname2")
        self.gridLayout.addWidget(self.itemname2, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
        self.itemeat1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.itemeat1.setObjectName("itemeat1")
        self.gridLayout.addWidget(self.itemeat1, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)
        self.itemid1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.itemid1.setObjectName("itemid1")
        self.gridLayout.addWidget(self.itemid1, 2, 2, 1, 1)
        self.itemeat2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.itemeat2.setObjectName("itemeat2")
        self.gridLayout.addWidget(self.itemeat2, 1, 3, 1, 1)
        self.itemname1 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.itemname1.setObjectName("itemname1")
        self.gridLayout.addWidget(self.itemname1, 0, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 1, 1, 1)
        self.package1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.package1.setObjectName("package1")
        self.gridLayout.addWidget(self.package1, 3, 2, 1, 1)
        self.package2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.package2.setObjectName("package2")
        self.gridLayout.addWidget(self.package2, 3, 3, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 70, 231, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pic1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.pic1.setObjectName("pic1")
        self.horizontalLayout.addWidget(self.pic1)
        self.pic2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.pic2.setObjectName("pic2")
        self.horizontalLayout.addWidget(self.pic2)
        # self.label_5 = QtWidgets.QLabel(Dialog)
        # self.label_5.setGeometry(QtCore.QRect(180, 370, 111, 21))
        # self.label_5.setObjectName("label_5")
        # self.pushButton = QtWidgets.QPushButton(Dialog)
        # self.pushButton.setGeometry(QtCore.QRect(290, 370, 75, 23))
        # self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setStyleSheet("background-color: #ffffff ;")
        from PyQt5.QtGui import QIcon
        Dialog.setWindowIcon(QIcon("util/huohuo.png"))
        # self.pushButton.clicked.connect(self.openPlantform)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "商品分析"))
        self.label.setText(_translate("Dialog", "情况概览"))
        self.itemid2.setText(_translate("Dialog", "TextLabel"))
        self.label_4.setText(_translate("Dialog", "名称"))
        self.label_7.setText(_translate("Dialog", "商店名称"))
        self.itemeat1.setText(_translate("Dialog", "TextLabel"))
        self.label_6.setText(_translate("Dialog", "食用方法"))
        self.itemid1.setText(_translate("Dialog", "TextLabel"))
        self.itemeat2.setText(_translate("Dialog", "TextLabel"))
        self.label_8.setText(_translate("Dialog", "包装形式"))
        self.package1.setText(_translate("Dialog", "3"))
        self.package2.setText(_translate("Dialog", "1"))
        self.pic1.setText(_translate("Dialog", "商品"))
        self.pic2.setText(_translate("Dialog", "商品"))
        # self.label_5.setText(_translate("Dialog", "更多详细信息点击"))
        # self.pushButton.setText(_translate("Dialog", "了解更多"))


    def PicShow(self):
        product_id1 = self.product_id1
        product_id2 = self.product_id2
        print("running pic show")
        from PyQt5.QtGui import QPixmap
        #图片展示
        image_path1 = f"Picture/{product_id1}.jpg"
        pixmap = QPixmap(image_path1)
        self.pic1.setPixmap(pixmap)
        self.pic1.setScaledContents(True)

        image_path2 = f"Picture/{product_id2}.jpg"
        pixmap = QPixmap(image_path2)
        self.pic2.setPixmap(pixmap)
        self.pic2.setScaledContents(True)

        #读取数据
        import os

        filename = f'jd.csv'
        directory = "Commodity"
        file_path = os.path.join(directory, filename)
        item_name1, otherinformation1 = self.read_csv(file_path,product_id1)
        item_name1 = item_name1.split(" ")[0].replace("商品名称：","")
        shopname1 = otherinformation1.split(",")[1].replace("店铺： ","")
        eatway1 = "——"
        package1 = "——"
        for item in otherinformation1.split(","):
            if "食用方法：" in item:
                eatway1 = item.replace("食用方法：","")
            if "包装形式：" in item:
                package1 = item.replace("包装形式：","")
        item_name2, otherinformation2 = self.read_csv(file_path,product_id2)
        item_name2 = item_name2.split(" ")[0].replace("商品名称：","")
        shopname2 = otherinformation2.split(",")[1].replace("店铺： ","")
        eatway2 = "——"
        package2 = "——"
        for item in otherinformation2.split(","):
            if "食用方法：" in item:
                eatway2 = item.replace("食用方法：","")
            if "包装形式：" in item:
                package2 = item.replace("包装形式：","")
        # shopname = otherinformation
        # print(item_name1)
        # print(shopname)
        # print(otherinformation)
        self.itemname1.setText(item_name1)
        self.itemid1.setText(shopname1)
        self.itemeat1.setText(eatway1)
        self.package1.setText(package1)


        self.itemname2.setText(item_name2)
        self.itemid2.setText(shopname2)
        self.itemeat2.setText(eatway2)
        self.package2.setText(package2)
    def read_csv(self, filename, ID):
        # data = []
        import csv
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) > 1 and ID in row[1]:
                    return row[0], row[2]
                # data.append(row)
        # return data


    def openPlantform(self):

        from Analysisplantform import AnalysisPlantform_Dialog
        # self.optimal_dialog = QDialog()
        # self.ui = AnalysisPlantform_Dialog()
        print(self.product_id1, self.product_id2)

        # self.ui.show_image_and_histogram("10072795033886","10099263767130")
        # self.ui.setupUi(self.optimal_dialog)
        # self.optimal_dialog.exec_()

        # self.Form = QtWidgets.QWidget()
        # ui = AnalysisPlantform_Dialog()
        # ui.setupUi(self.Form)
        # ui.show_image_and_histogram(self.product_id1,self.product_id2)
        # self.Form.show()


        dialog = QDialog()

        # 使用 Sale_Form 类来设置界面
        ui = AnalysisPlantform_Dialog()
        ui.setupUi(dialog)
        ui.show_image_and_histogram(self.product_id1, self.product_id1)
        # 显示对话框
        dialog.exec_()

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)

    # 创建一个 QDialog 对象来显示界面
    dialog = QDialog()

    # 使用 Sale_Form 类来设置界面
    ui = detailinformation_Dialog("10072795033886","10099263767130")
    ui.setupUi(dialog)
    # ui.PicShow()
    # ui.openPlantform()
    # 显示对话框
    dialog.show()

    sys.exit(app.exec_())