import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.uic import loadUi
import time
from PyQt5 import QtCore

class Buy_Form3(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 200, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))


# 第二个窗口的界面类
class Buy_Form(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 200, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.show_second_window)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))

    def show_second_window(self):
        # 创建并显示第二个窗口
        dialog = QDialog()
        ui = Buy_Form3()
        ui.setupUi(dialog)
        dialog.exec_()


# 线程工作类
class Worker(QObject):
    finished = pyqtSignal()

    def run(self):
        # 模拟耗时操作
        time.sleep(2)
        self.finished.emit()

# class Mainwindows(object):
#     def setupUi(self, Form):
#         # 界面布局等设置
#         self.pushButton = QPushButton(Form)
#         self.pushButton.setGeometry(QtCore.QRect(150, 100, 93, 28))
#         self.pushButton.setObjectName("pushButton")
#
#
#         self.pushButton.clicked.connect(self.open_second_window)
#         # 初始化线程和工作对象
#         self.worker = Worker()
#         self.thread = QThread()
#         self.worker.moveToThread(self.thread)
#         self.worker.finished.connect(self.show_second_window)
#         self.thread.started.connect(self.worker.run)
#
#
#
#     def open_second_window(self):
#         # 启动线程执行耗时操作
#         self.thread.start()
#
#     def show_second_window(self):
#         # 创建并显示第二个窗口
#         dialog = QDialog()
#         ui = Buy_Form()
#         ui.setupUi(dialog)
#         dialog.exec_()

class Mainwindows(object):
    def setupUi(self, Form):
        # 界面布局等设置
        self.pushButton = QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 100, 93, 28))
        self.pushButton.setObjectName("pushButton")


        self.pushButton.clicked.connect(self.open_second_window)

    def open_second_window(self):
        # 创建并启动线程执行耗时操作
        self.worker = Worker()
        self.thread = QThread()
        self.worker.moveToThread(self.thread)
        self.worker.finished.connect(self.show_second_window)
        self.thread.started.connect(self.worker.run)
        self.thread.start()

    def show_second_window(self):
        # 创建并显示第二个窗口
        dialog = QDialog()
        ui = Buy_Form()
        ui.setupUi(dialog)
        dialog.exec_()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QDialog()
    ui = Mainwindows()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
