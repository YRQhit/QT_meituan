# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optimal3.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import time
import sys
import csv
class getAdvantage_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(547, 502)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 30, 180, 20))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 60, 461, 200))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setFixedSize(200, 200)
        self.horizontalLayout.addWidget(self.label_2)
        self.textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        # self.textEdit.setFixedSize(300, 300)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setPlaceholderText("商品信息")
        self.horizontalLayout.addWidget(self.textEdit)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 350, 381, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.EmotionScore = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.EmotionScore.setObjectName("EmotionScore")
        self.gridLayout.addWidget(self.EmotionScore, 1, 0, 1, 1)
        # self.LDA = QtWidgets.QPushButton(self.gridLayoutWidget)
        # self.LDA.setObjectName("LDA")
        # self.gridLayout.addWidget(self.LDA, 0, 0, 1, 1)
        # self.KeyWord = QtWidgets.QPushButton(self.gridLayoutWidget)
        # self.KeyWord.setObjectName("KeyWord")
        # self.gridLayout.addWidget(self.KeyWord, 0, 1, 1, 1)
        self.Suggestion = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Suggestion.setObjectName("Suggestion")
        self.gridLayout.addWidget(self.Suggestion, 1, 1, 1, 1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(80, 290, 371, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("输入商品对应的URL")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.GetData = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.GetData.setObjectName("GetData")
        self.horizontalLayout_2.addWidget(self.GetData)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(430, 40, 54, 12))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(13)
        self.label.setFont(font)
        # 按钮信号

        # if self.GetData.isDown():
        #     print("按钮被按下了！")

        self.GetData.clicked.connect(self.SpyderPart)

        # self.LDA.clicked.connect(self.ldabutton)
        # self.KeyWord.clicked.connect(self.ciyun)

        self.EmotionScore.clicked.connect(self.emotionscore)
        self.Suggestion.clicked.connect(self.suggestion)
        Dialog.setStyleSheet("background-color: #ffffff ;")
        from PyQt5.QtGui import QIcon
        Dialog.setWindowIcon(QIcon("util/huohuo.png"))
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "优化平台"))
        self.label.setText(_translate("Dialog", "一键获得优缺点平台"))
        self.label_2.setText(_translate("Dialog", "图片"))
        self.EmotionScore.setText(_translate("Dialog", "评论感情分"))
        # self.LDA.setText(_translate("Dialog", "评论内容分类概览"))
        # self.KeyWord.setText(_translate("Dialog", "评论信息关键词"))
        self.Suggestion.setText(_translate("Dialog", "商品优缺点"))
        self.GetData.setText(_translate("Dialog", "获取商品数据"))
        self.label_3.setText(_translate("Dialog", "已完成"))


    def SpyderPart(self):
        #采用多线程
        self.label_3.setText("运行中")
        text = self.lineEdit.text()
        import re
        product_id = re.search(r'\d+', text).group()

        print("Text from QLineEdit:", text)
        print("商品ID{},".format(product_id) )


        from threading import Thread
        from GetInformationPart import commentSpider,GetBaseinformation
        # 创建 Thread 实例
        comment = commentSpider(product_id)
        information = GetBaseinformation(product_id)
        result = information.analysis_page(information.get_page())
        # comment.run()

        t1 = Thread(target = information.analysis_page(information.get_page()), args = ('第一个线程', 1))
        t2 = Thread(target = comment.run(), args = ('第二个线程', 2))
        # 启动线程运行
        t1.start()
        t2.start()

        # 等待所有线程执行完毕
        t1.join()  # join() 等待线程终止，要不然一直挂起
        t2.join()

        print("数据下载完毕")
        print("显示数据")


        from PyQt5.QtGui import QPixmap

        #jpg显示
        image_path = f"Picture/{product_id}.jpg"
        # image_path = f"images/{selected_option.lower()}.jpg"  # 假设图片路径与选项名字相同
        pixmap = QPixmap(image_path)
        self.label_2.setPixmap(pixmap)
        self.label_2.setScaledContents(True)

        #
        print(result)
        self.textEdit.setText(result)
        self.label_3.setText("已完成")


    def ldabutton(self):
        from LDAPart import LDA
        print("LDA运行")
        self.lda = LDA()
        self.label_3.setText("运行中")
        text = self.lineEdit.text()
        import re
        product_id = re.search(r'\d+', text).group()

        self.lda.run(product_id)
        print("计算完成")
        self.lda.openHTML(product_id)
        print("打开html")
        self.label_3.setText("运行完成")

    def ciyun(self):
        print("词云运行")
        self.label_3.setText("运行中")
        text = self.lineEdit.text()
        import re
        product_id = re.search(r'\d+', text).group()
        from ciyun import WordCloudDialog
        self.worldcloud = WordCloudDialog(product_id)
        self.worldcloud.exec_()
        # self.worldcloud.show()

        self.label_3.setText("运行完成")


    def emotionscore(self):
        print("进行情感分析")
        self.label_3.setText("运行中")
        import emtionPart

        text = self.lineEdit.text()
        import re
        import os
        ID = re.search(r'\d+', text).group()

        emtionPart.test_jd(ID)

        def read_csv(filename):
            data = []
            with open(filename, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    data.append(row)
            return data

        # app = QApplication(sys.argv)
        self.emotion = emtionPart.EmotionScore()

        filename = f'{ID}.csv'
        directory = "emotionScore"
        file_path = os.path.join(directory, filename)
        data = read_csv(file_path)
        self.emotion.load_data(data)
        self.emotion.show_snowNLP_distribution(data, ID)
        self.emotion.exec_()
        print("运行完成")
        self.label_3.setText("运行完成")

    def suggestion(self):
        # from suggestionPart import TextDialog
        # text = self.lineEdit.text()
        # import re
        # import os
        # ID = re.search(r'\d+', text).group()
        # print(ID)
        # self.dialog = QDialog()
        # ui = Suggest_Dialog()
        # ui.setupUi(self.dialog, ID)
        #
        # # 显示对话框
        # self.dialog.exec_()

        # widget = TextDialog(ID)
        # widget.show()

        from suggestionPart import Suggest_Dialog
        text = self.lineEdit.text()
        import re
        import os
        ID = re.search(r'\d+', text).group()

        self.dialog = QDialog()
        ui = Suggest_Dialog()
        ui.setupUi(self.dialog, ID)
        # 显示对话框
        self.dialog.exec_()


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)

    # 创建一个 QDialog 对象来显示界面
    dialog = QDialog()

    # 使用 Sale_Form 类来设置界面
    ui = getAdvantage_Dialog()
    ui.setupUi(dialog)

    # 显示对话框
    dialog.show()

    sys.exit(app.exec_())