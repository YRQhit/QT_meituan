# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recomand.ui'
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
import os
class recommand_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(518, 407)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 330, 311, 73))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.url = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.url.setObjectName("url")
        self.url.setFixedSize(311, 20)
        self.horizontalLayout.addWidget(self.url)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(90, 100, 301, 111))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pic = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.pic.setObjectName("pic")
        self.pic.setFixedSize(111, 111)
        self.horizontalLayout_2.addWidget(self.pic)
        self.information = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_2)
        self.information.setObjectName("information")
        self.horizontalLayout_2.addWidget(self.information)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 240, 301, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.text2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.text2.setObjectName("text2")
        self.gridLayout.addWidget(self.text2, 1, 1, 1, 1)
        self.title1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.title1.setObjectName("title1")
        self.gridLayout.addWidget(self.title1, 0, 0, 1, 1)
        self.text1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.text1.setObjectName("text1")
        self.gridLayout.addWidget(self.text1, 0, 1, 1, 1)
        self.title2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.title2.setObjectName("title2")
        self.gridLayout.addWidget(self.title2, 1, 0, 1, 1)
        self.title3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.title3.setObjectName("title3")
        self.gridLayout.addWidget(self.title3, 2, 0, 1, 1)
        self.text3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.text3.setObjectName("text3")
        self.gridLayout.addWidget(self.text3, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(130, 20, 201, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(36)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        itemname , itemid , iteminformation , imgPath ,itemprice= self.getPersonallike()
        ID = itemid.replace("商品编号：","")

        if os.path.exists(imgPath):
            print("图片已被下载")
        else:
            self.download_image(imgPath, ID)

        from PyQt5.QtGui import QPixmap

        # jpg显示
        image_path = f"Picture/{ID}.jpg"
        # image_path = f"images/{selected_option.lower()}.jpg"  # 假设图片路径与选项名字相同
        pixmap = QPixmap(image_path)
        self.pic.setPixmap(pixmap)
        self.pic.setScaledContents(True)

        self.information.setText(itemname)

        url = "https://item.jd.com/{}.html".format(ID)

        # self.text1.setText(itemprice)
        # self.title1.setText("价格")
        # iteminformation.split(",")
        # for item in iteminformation.split(",")[1:]:
        #
        #     self.title1.setText(item.split(":")[0])
        #     self.text1.setText(item.split("")[1])
        for i, item in enumerate(iteminformation.split(",")[1:]):
            if 0 <= i <= 2:
                title = item.split("：")[0]
                text = item.split("：")[1]

                # 根据索引动态构造标签对象的名称
                title_label_name = f"title{i + 1}"
                text_label_name = f"text{i + 1}"

                # 获取标签对象
                title_label = getattr(self, title_label_name)
                text_label = getattr(self, text_label_name)

                # 设置标签对象的文本内容
                title_label.setText(title)
                text_label.setText(text)

        if len(iteminformation.split(",")[1:])<3:
            self.text3.setText(itemprice)
            self.title3.setText("价格")
        #显示url
        self.url.setText(url)

        Dialog.setStyleSheet("background-color: #ffffff ;")
        from PyQt5.QtGui import QIcon
        Dialog.setWindowIcon(QIcon("util/huohuo.png"))

    def download_image(self, url, filename):
        from PIL import Image
        import pillow_avif
        import requests
        send_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
            "Connection": "keep-alive",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8"}

        response = requests.get(url, headers=send_headers)
        if response.status_code == 200:
            # 写入文件
            filename = f"{filename}.jpg"
            directory = "Picture"
            PicPath = os.path.join(directory, filename)
            with open(PicPath, 'wb') as f:
                f.write(response.content)
            # avif文件
            # print("图片下载成功")
            # AVIFfilename = PicPath
            # AVIFimg = Image.open(AVIFfilename)
            # AVIFimg.save(AVIFfilename.replace("avif", 'jpg'), 'JPEG')
        else:
            print("下载失败，HTTP 状态码:", response.status_code)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "商品url"))
        self.pic.setText(_translate("Dialog", "TextLabel"))
        self.text2.setText(_translate("Dialog", "TextLabel"))
        self.title1.setText(_translate("Dialog", "TextLabel"))
        self.text1.setText(_translate("Dialog", "TextLabel"))
        self.title2.setText(_translate("Dialog", "TextLabel"))
        self.title3.setText(_translate("Dialog", "TextLabel"))
        self.text3.setText(_translate("Dialog", "TextLabel"))
        self.label_9.setText(_translate("Dialog", "好物推荐"))

    def read_csv(self, filename):
        import csv
        data = []
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
        return data

    def get_files_in_folder(self, folder_path):
        # 检查文件夹路径是否存在
        import os
        if not os.path.isdir(folder_path):
            print("指定的路径不是文件夹。")
            return

        # 获取文件夹下的所有文件名称
        files = os.listdir(folder_path)

        # 打印文件名称
        ID = []
        for file in files:
            ID.append(file.split(".")[0])
        return ID

    def getPersonallike(self):
        import os
        filepath = os.path.join("Commodity", "预制菜.csv")
        # 得到我们浏览历史数据
        readInformation = []
        Totledata = self.read_csv(filepath)
        for item in Totledata:#假设emotionScore中是顾客喜欢的商品,也就是浏览的历史记录
            if item[6] in self.get_files_in_folder("./emotionScore"):
                readInformation.append(item)
        # print(readInformation)
        print(self.get_files_in_folder("./emotionScore"))
        totleprice = 0
        shop = set()
        for data in readInformation:
            totleprice = totleprice + float(data[1])
            shop.add(data[2])
        average = totleprice/len(readInformation)#商品消费水平
        # print(average,shop)

        filepath2 = os.path.join("Commodity", "jd.csv")
        detail = self.read_csv(filepath2)
        # otherInformation = set()
        otherInformation = []
        for item in detail:#在详细数据中获得其他的属性
            if item[1].replace("商品编号：","") in self.get_files_in_folder("./emotionScore"):
                # print(item[2].split(",")[2:])
                # temp = set(item[2].split(",")[2:])
                # otherInformation.update(temp)
                otherInformation.extend(item[2].split(",")[2:])

        print(otherInformation)
        from collections import Counter
        counter = Counter(otherInformation)
        print(counter)#属性页面
        import random
        for item in detail:
            if abs(average - float(item[4])) < random.randint(0,10) and counter.most_common(3)[random.randint(0,2)][0] in item[2] and item[1].replace("商品编号：","") not in self.get_files_in_folder("./emotionScore"):
                print(random.randint(0,10),counter.most_common(2)[0][0])
                return item[0], item[1], item[2], item[3], item[4]








if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)

    # 创建一个 QDialog 对象来显示界面
    dialog = QDialog()

    # 使用 Sale_Form 类来设置界面
    ui = recommand_Dialog()
    ui.setupUi(dialog)
    #得到用户看到的数据
    # print(ui.get_files_in_folder("./Picture"))
    #
    # import os
    # filepath = os.path.join("Commodity","预制菜.csv")
    # print(ui.read_csv(filepath))
    # readInformation = []
    # for item in ui.read_csv(filepath):
    #     if item[6] in ui.get_files_in_folder("./Picture"):
    #         readInformation.append(item)
    # print(readInformation)
    # ui.getPersonallike()
    # 显示对话框
    dialog.show()

    sys.exit(app.exec_())