import csv
import os
import pandas as pd
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel
import sys
import json
class TextDialog(QDialog):
    def __init__(self,ID):
        super().__init__()
        self.setWindowTitle('评论页面')
        self.layout = QVBoxLayout(self)
        text = self.getTEXT(ID)
        self.process_text(text)

    def process_text(self, data):
        content = data['data']['choices'][0]['content']
        advantages, disadvantages = self.extract_advantages_and_disadvantages(content)

        self.layout.addWidget(QLabel('优点：'))
        for advantage in advantages:
            self.layout.addWidget(QLabel(advantage))

        self.layout.addWidget(QLabel('缺点：'))
        for disadvantage in disadvantages:
            self.layout.addWidget(QLabel(disadvantage))

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

        question = getText("user", "分点概述，从下面的评论中得到这个产品的优势和缺点,给出商品改进建议"+comment)
        response = zhipuai.model_api.invoke(
            model=model,
            prompt=question
        )
        print(response)
        return response

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = TextDialog("10099263767130")
    widget.show()
    sys.exit(app.exec_())
