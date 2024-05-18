import csv
import os
import pandas as pd
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel
import sys
import json

from PyQt5 import QtCore, QtGui, QtWidgets
# class Suggest_Dialog(object):
#     def setupUi(self, Dialog, ID):
#         # self.setWindowTitle('评论页面')
#         Dialog.setObjectName("AI 小助手")
#         Dialog.resize(500, 500)
#
#         self.label = QtWidgets.QLabel(Dialog)
#         # self.label.setGeometry(QtCore.QRect(0,0, 350, 100))
#         self.label.setObjectName("label")
#         # self.layout = QVBoxLayout(self)
#         text = self.getTEXT(ID)
#         self.process_text(text)
#         QtCore.QMetaObject.connectSlotsByName(Dialog)
#         # 设置样式表
#         Dialog.setStyleSheet("background-color: #ffffff ;")
#         from PyQt5.QtGui import QIcon
#         Dialog.setWindowIcon(QIcon("util/huohuo.png"))
#     def retranslateUi(self, Dialog):
#         _translate = QtCore.QCoreApplication.translate
#         Dialog.setWindowTitle(_translate("Dialog", "智能小助手"))
class Suggest_Dialog(object):
    def setupUi(self, Dialog, ID):
        # 设置窗口标题为 "智能小助手"
        Dialog.setWindowTitle("智能小助手")
        Dialog.setObjectName("AI 小助手")
        Dialog.resize(500, 500)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")

        text = self.getTEXT(ID)
        self.process_text(text)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setStyleSheet("background-color: #ffffff ;")
        from PyQt5.QtGui import QIcon
        Dialog.setWindowIcon(QIcon("util/huohuo.png"))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "智能小助手"))
    def process_text(self, data):
        content = data['data']['choices'][0]['content']
        advantages, disadvantages = self.extract_advantages_and_disadvantages(content)
        advresult = ""
        disadvresult = ""
        for adv in advantages:
            advresult = advresult +"\n" + adv
        for disadv in disadvantages:
            disadvresult = disadvresult + "\n" + disadv
        self.label.setText("优点有:"+advresult + "\n" + "缺点有:" + disadvresult)
        # self.layout.addWidget(QLabel())
        # for advantage in advantages:
        #     self.layout.addWidget(QLabel(advantage))
        #
        # self.layout.addWidget(QLabel('缺点：'))
        # for disadvantage in disadvantages:
        #     self.layout.addWidget(QLabel(disadvantage))

    def extract_advantages_and_disadvantages(self, text):
        parts = text.split('\\n\\n缺点：\\n')
        advantages = parts[0].split('\\n')[1:]
        disadvantages = parts[1].split('\\n')[0:]
        return advantages, disadvantages

    def getTEXT(self,ID):
        Excelfile = './LDA/result/{}.xlsx'.format(ID)
        df = pd.read_excel(Excelfile)
        topic = df['topic']
        # print(topic)
        zero_rows = df[df['topic'] == 0].index.tolist()  # 将'column_name'替换为你要筛选的列名
        # print(zero_rows)


        import random
        SampleData = []
        # 提取某一列等于0的行
        for j in range(7):
            try:
                zero_rows = df[df['topic'] == j]  # 将'column_name'替换为你要筛选的列名
                # 随机选取10行数据
                sampled_rows_0 = random.sample(zero_rows.index.tolist(), k=5)

                # print(sampled_rows)

                sampled_data_0 = df.loc[sampled_rows_0, ['评论内容']]  # 替换为其他列名

                print(sampled_data_0)

                for i in range(len(sampled_data_0)):
                    SampleData.append(sampled_data_0.iloc[i, 0])
            except:
                pass


        # print(SampleData)
        comment = "".join(SampleData)
        print("从下面的评论中得到这个产品的优势和缺点:"+comment)

        import zhipuai
        zhipuai.api_key ="a2c3696675d0914c53ce693fd9ab51a2.mHp0Uz5xbTB9OHAL"#填写控制台中获取的 APIKey 信息
        model ="chatglm_std"#用于配置大模型版本

        def getText(role, content, text = []):
            # role 是指定角色，content 是 prompt 内容
            jsoncon = {}
            jsoncon["role"] = role
            jsoncon["content"] = content
            text.append(jsoncon)
            return text

        question = getText("user", "分点概述，从下面的评论中得到这个产品的优势和缺点"+comment)
        response = zhipuai.model_api.invoke(
            model=model,
            prompt=question
        )
        print(response)
        return response

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # widget = Suggest_Dialog("10099263767130")
    # widget.show()
    ID = "10099263767130"
    dialog = QDialog()
    ui = Suggest_Dialog()
    ui.setupUi(dialog, ID)
    dialog.show()
    sys.exit(app.exec_())
