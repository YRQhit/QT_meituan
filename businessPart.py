import sys
from PyQt5.QtWidgets import QApplication, QComboBox, QCompleter, QVBoxLayout, QWidget, QLineEdit, QPushButton, QHBoxLayout, QTextEdit, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import os
import csv
class SearchableComboBoxWidget(QWidget):
    def __init__(self, parent=None):
        super(SearchableComboBoxWidget, self).__init__(parent)
        layout = QVBoxLayout()
        self.setWindowTitle("评论分析页面")
        self.setFixedSize(800, 1000)
        self.combo_box = QComboBox()
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("输入商品ID")  # 添加灰色提示输入

        #获得下载好的评论信息
        file = self.GetID()
        ids = [self.extract_id(file_path) for file_path in file]
        # print(ids)
        options = ids
        # options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]
        self.combo_box.addItems(options)

        completer = QCompleter(options)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.search_box.setCompleter(completer)

        layout.addWidget(self.search_box)

        button_layout = QHBoxLayout()
        self.ok_button = QPushButton("OK")
        button_layout.addWidget(self.ok_button)
        button_layout.addStretch(1)  # 添加拉伸因子使按钮位于右侧

        layout.addLayout(button_layout)


        #修改显示为水平
        # self.image_label = QLabel()
        # layout.addWidget(self.image_label)
        # self.setLayout(layout)
        #
        # self.display_box = QTextEdit()
        # layout.addWidget(self.display_box)
        # self.setLayout(layout)

        # 创建水平布局

        hbox_layout = QHBoxLayout()
        self.image_label = QLabel()
        self.image_label.setFixedSize(300, 300)
        hbox_layout.addWidget(self.image_label)
        self.display_box = QTextEdit()
        self.display_box.setFixedSize(300, 200)
        hbox_layout.addWidget(self.display_box)

        # 将水平布局添加到垂直布局中
        layout.addLayout(hbox_layout)
        self.setLayout(layout)



        #LDA展示
        hbox_layout_2 = QHBoxLayout()
        LDA_button_layout = QHBoxLayout()
        self.LDA_button = QPushButton("LDA计算")
        LDA_button_layout.addWidget(self.LDA_button)
        LDA_button_layout.addStretch(1)  # 添加拉伸因子使按钮位于右侧
        # layout.addLayout(LDA_button_layout)
        hbox_layout_2.addLayout(LDA_button_layout)

        LDA_button_layout = QHBoxLayout()
        self.LDA_buttonShow = QPushButton("LDA可视化展示")
        LDA_button_layout.addWidget(self.LDA_buttonShow)
        LDA_button_layout.addStretch(1)  # 添加拉伸因子使按钮位于右侧
        # layout.addLayout(LDA_button_layout)
        hbox_layout_2.addLayout(LDA_button_layout)

        layout.addLayout(hbox_layout_2)
        # 词频展示
        Word_button_layout = QHBoxLayout()
        self.Word_button = QPushButton("词频展示")
        Word_button_layout.addWidget(self.Word_button)
        Word_button_layout.addStretch(1)  # 添加拉伸因子使按钮位于右侧
        layout.addLayout(Word_button_layout)



        # 情感数据展示
        hbox_layout_2 = QHBoxLayout()
        Emotion_button_layout = QHBoxLayout()
        self.Emotion_button = QPushButton("情感值展示")
        Emotion_button_layout.addWidget(self.Emotion_button)
        Emotion_button_layout.addStretch(1)  # 添加拉伸因子使按钮位于右侧
        hbox_layout_2.addLayout(Emotion_button_layout)

        Emotion_button_layout = QHBoxLayout()
        self.Emotion_button_show = QPushButton("情感值展示")
        Emotion_button_layout.addWidget(self.Emotion_button_show)
        Emotion_button_layout.addStretch(1)  # 添加拉伸因子使按钮位于右侧
        hbox_layout_2.addLayout(Emotion_button_layout)

        layout.addLayout(hbox_layout_2)
        # 图片展示
        PIC_button_layout = QHBoxLayout()
        self.PIC_button = QPushButton("图片信息模块")
        PIC_button_layout.addWidget(self.PIC_button)
        PIC_button_layout.addStretch(1)  # 添加拉伸因子使按钮位于右侧
        layout.addLayout(PIC_button_layout)

        # 建议模块展示
        Advice_button_layout = QHBoxLayout()
        self.Advice_button = QPushButton("建议模块")
        Advice_button_layout.addWidget(self.Advice_button)
        Advice_button_layout.addStretch(1)  # 添加拉伸因子使按钮位于右侧
        layout.addLayout(Advice_button_layout)

        self.setLayout(layout)

        self.search_box.textChanged.connect(self.search_text_changed)
        self.combo_box.currentTextChanged.connect(self.combo_box_text_changed)

        self.ok_button.clicked.connect(self.ok_button_clicked)
        #词云
        self.Word_button.clicked.connect(self.WorldCloud)
        #LDA
        self.LDA_button.clicked.connect(self.LDA)
        self.LDA_buttonShow.clicked.connect(self.LDAShow)
        #情感值
        self.Emotion_button.clicked.connect(self.emotion)
        self.Emotion_button_show.clicked.connect(self.emotionShow)

        #图片展示模块
        self.PIC_button.clicked.connect(self.PICShow)

        #建议模块
        self.Advice_button.clicked.connect(self.SuggestionShow)

        # TEST
        # file = self.GetID()
        # ids = [self.extract_id(file_path) for file_path in file]
        # print(ids)
        # self.openCSV(6, '100084057740', [1, 2])

    def search_text_changed(self, text):
        index = self.combo_box.findText(text)
        if index != -1:
            self.combo_box.setCurrentIndex(index)

    def combo_box_text_changed(self, text):
        self.search_box.setText(text)

    def ok_button_clicked(self):
        selected_option = self.combo_box.currentText()
        #selected_option是商品ID
        commodity_info = self.openCSV(6, selected_option, [0, 1, 2])
        self.display_box.append("产品名称: " + commodity_info[0][0])
        self.display_box.append("产品价格: " + commodity_info[0][1])
        self.display_box.append("店铺名称 " + commodity_info[0][2])
        # print(self.openCSV(6, selected_option, [0, 1, 2]))

        selected_option = self.combo_box.currentText()
        #测试图片

        image_path = f"Picture/{selected_option}.jpg"
        # image_path = f"images/{selected_option.lower()}.jpg"  # 假设图片路径与选项名字相同
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)

    #获得爬取的评论数据
    def GetID(self):
        directory = "./comments"
        files = []
        for root, dirs, filenames in os.walk(directory):
            for filename in filenames:
                # 将文件的绝对路径添加到列表中
                files.append(os.path.join(root, filename))

        print(files)
        return files

    #提取id
    def extract_id(self, file_path):
        # 使用split()方法将路径分割成目录和文件名
        filename = os.path.split(file_path)[1]
        # 使用split()方法将文件名按等号分割成两部分，并取第二部分作为ID
        id = filename.split('=')[1].split('.')[0]
        return id

    #打开csv文件
    def openCSV(self, search_column, search_value, return_columns):
        keyword = "预制菜"
        filename = f'{keyword}-jd.csv'
        directory = "Commodity"
        file_path = os.path.join(directory, filename)
        data = []
        # columns = [0, 1, 2, 6]
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                # 仅提取指定列的数据
                if row[search_column] == search_value:
                    result = {}
                    # 获取其他指定列的数据
                    for column in return_columns:
                        result[column] = row[column]
                    data.append(result)
        return data

    # def OpenPic(self):


    def WorldCloud(self):

        ID = self.combo_box.currentText()
        # app = QApplication(sys.argv)
        self.worldcloud = WordCloudDialog(ID)
        self.worldcloud.show()
        # sys.exit(app.exec_())

    def LDA(self):
        lda = LDA()
        ID = self.combo_box.currentText()
        lda.run(ID)
        # lda.openHTML(ID)
    def LDAShow(self):
        ID = self.combo_box.currentText()
        lda = LDA()
        lda.openHTML(ID)


    def emotion(self):
       import emtionPart
       ID = self.combo_box.currentText()
       emtionPart.test_jd(ID)
       # print("")

    def emotionShow(self):
        def read_csv(filename):
            data = []
            with open(filename, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    data.append(row)
            return data

        # app = QApplication(sys.argv)
        emotion = EmotionScore()
        ID = self.combo_box.currentText()
        filename = f'{ID}.csv'
        directory = "emotionScore"
        file_path = os.path.join(directory, filename)
        data = data = read_csv(file_path)
        emotion.load_data(data)
        emotion.exec_()

    def PICShow(self):
        from PicturePart import ImageDialog
        ID = self.combo_box.currentText()
        window = ImageDialog()
        window.show_image_and_histogram(ID)
        # sys.exit(app.exec_())


    def SuggestionShow(self):
        print("start")
        from suggestionPart import TextDialog
        ID = self.combo_box.currentText()
        self.widget = TextDialog(ID)
        self.widget.show()
        # sys.exit(app.exec_())

import os
import pandas as pd
import re
import jieba
import jieba.posseg as psg

#LDA部分
class LDA():
    import os
    def chinese_word_cut(self, mytext):

        # root_dir = os.getcwd()
        #
        # dic_file = os.path.join(root_dir, r",\stopWord\dict.txt")

        dic_file = r".\stopWord\dict.txt"
        stop_file = r".\stopWord\fourStopwords.txt"
        jieba.load_userdict(dic_file)  # 加载用户词典
        jieba.initialize()  # 手动初始化（可选）

        # 加载用户停用词表
        try:
            stopword_list = open(stop_file, encoding='utf-8')
        except:
            stopword_list = []
            print("error in stop_file")

        stop_list = []  # 存储用户停用词
        flag_list = ['n', 'nz', 'vn']  # 指定在jieba.posseg分词函数中只保存n：名词、nz：其他专名、vn：动名词
        for line in stopword_list:
            line = re.sub(u'\n|\\r', '', line)
            stop_list.append(line)

        word_list = []
        seg_list = psg.cut(mytext)  # jieba.posseg分词

        # 原称之为粑粑山型的 词语过滤
        for seg_word in seg_list:
            word = re.sub(u'[^\u4e00-\u9fa5]', '', seg_word.word)  # 只匹配所有中文
            find = 0  # 标志位
            for stop_word in stop_list:
                if stop_word == word or len(word) < 2:  # 长度小于2或者在用户停用词表中，将被过滤
                    find = 1
                    break
            if find == 0 and seg_word.flag in flag_list:  # 标志位为0且是需要的词性则添加至word_list
                word_list.append(word)
        return (" ").join(word_list)
    def run(self, ID):
        if os.path.exists(".\\LDA\\result\\{}.html".format(ID)):
            print("the files have been calculated")
            pass
        else:
            data = pd.read_csv('.\comments\productId={}.csv'.format(ID))

            data["content_cutted"] = data.评论内容.apply(self.chinese_word_cut)

            from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
            from sklearn.decomposition import LatentDirichletAllocation

            # 在notebook中展示一下LDA分析结果，可去除
            def print_top_words(model, feature_names, n_top_words):
                tword = []
                for topic_idx, topic in enumerate(model.components_):
                    print("Topic #%d:" % topic_idx)
                    topic_w = " ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]])
                    tword.append(topic_w)
                    print(topic_w)
                return tword

            n_features = 1000  # 提取1000个特征词语
            tf_vectorizer = CountVectorizer(strip_accents='unicode',
                                            max_features=n_features,
                                            stop_words='english',
                                            max_df=0.5,
                                            min_df=10)
            tf = tf_vectorizer.fit_transform(data.content_cutted)
            n_topics = 7  # 手动指定分类数
            lda = LatentDirichletAllocation(n_components=n_topics, max_iter=50,
                                            learning_method='batch',
                                            learning_offset=50,
                                            doc_topic_prior=0.1,
                                            topic_word_prior=0.01,
                                            random_state=0)
            lda.fit(tf)

            LatentDirichletAllocation(doc_topic_prior=0.1, learning_offset=50, max_iter=50,
                                      n_components=7, random_state=0,
                                      topic_word_prior=0.01)

            n_top_words = 25
            tf_feature_names = tf_vectorizer.get_feature_names_out()
            topic_word = print_top_words(lda, tf_feature_names, n_top_words)

            import numpy as np

            topics = lda.transform(tf)
            topic = []

            # output_path = r'.\LDA\result'
            # os.chdir(output_path)

            for t in topics:
                topic.append(list(t).index(np.max(t)))
            data['topic'] = topic
            data.to_excel(".\\LDA\\result\\{}.xlsx".format(ID), index=False)

            import pyLDAvis
            import pyLDAvis.sklearn
            # pyLDAvis.enable_notebook()                                  #在notebook中展示
            pic = pyLDAvis.sklearn.prepare(lda, tf, tf_vectorizer)
            pyLDAvis.save_html(pic, '.\\LDA\\result\\' + ID + '.html')

    def openHTML(self,ID):
        import webbrowser
        # currentPATH = os.getcwd()
        # print(currentPATH)

        output_path = r'.\LDA\result'
        # os.chdir(output_path)

        # print(os.path.join(output_path, "{}.html".format(ID)))
        file_path = os.path.join(output_path, "{}.html".format(ID))
        webbrowser.open(file_path)



from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QWidget, QPushButton, QLabel, QScrollArea, QComboBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from ciyun import WordCloud
from collections import Counter
#词云部分

class WordCloudWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)

class WordListWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

    def display_wordlist(self, word_dict):
        self.clear_layout()
        for word, freq in word_dict.items():
            label = QLabel(f"{word}: {freq}")
            self.layout.addWidget(label)

    def clear_layout(self):
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

class WordCloudDialog(QDialog):
    def __init__(self, ID):
        super().__init__()
        self.setWindowTitle("WordCloud in QDialog")
        #图片
        self.wordcloudWidget = WordCloudWidget()
        #词频列表
        self.wordlistWidget = WordListWidget()
        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.wordlistWidget)

        # self.comboBox = QComboBox()
        # self.comboBox.addItem("词频")
        # self.comboBox.addItem("情感")
        #
        # self.comboBox.currentTextChanged.connect(self.display_data)

        self.button = QPushButton("Close")
        self.button.clicked.connect(self.close)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.addWidget(self.wordcloudWidget)
        self.horizontalLayout.addWidget(self.scrollArea)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.addLayout(self.horizontalLayout)
        # self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout.addWidget(self.button)
        self.setLayout(self.verticalLayout)

        # layout = QVBoxLayout()
        # layout.addWidget(self.wordcloudWidget)
        # # layout.addWidget(self.comboBox)
        # layout.addWidget(self.scrollArea)
        # layout.addWidget(self.button)
        # self.setLayout(layout)

        # Generate wordcloud
        self.generate_wordcloud(ID)

    def generate_wordcloud(self, ID):
        filename = f'productId={ID}.csv'
        directory = "comments"
        file_path = os.path.join(directory, filename)

        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            comment = []
            for row in csv_reader:
                try:
                    comment.append(row[1])
                except:
                    # print(row)
                    pass

        One_file_word_array = []
        emotion = 0

        for com in comment:
            if com != [] and com != "评论内容":
                seg_list = jieba.cut(com, cut_all=False)
                word_list = list(seg_list)

                from string import punctuation
                from zhon.hanzi import punctuation
                import re

                filename = f'fourStopwords.txt'
                directory = "stopWord"
                file_path = os.path.join(directory, filename)

                fourStopwords = open(file_path, "r", encoding='utf-8').read()
                stopwords = fourStopwords.split("\n")

                text = re.sub("[{}]+".format(punctuation), "", com)
                seg_list = jieba.cut(com, cut_all=False)
                word_list = list(seg_list)
                One_file_word_array = word_list + One_file_word_array

        cut_stop_data = [word for word in One_file_word_array if word not in stopwords]
        word_count = Counter(cut_stop_data)
        word_dict = dict(word_count)
        word_dict = {word.replace("\n", ""): freq for word, freq in word_dict.items()}

        font_path = "simsun.ttf"
        wordcloud = WordCloud(font_path=font_path, background_color="white")
        wordcloud.generate_from_frequencies(word_dict)

        self.wordcloudWidget.figure.clear()
        ax = self.wordcloudWidget.figure.add_subplot(111)
        ax.imshow(wordcloud, interpolation="bilinear")
        ax.axis("off")
        self.wordcloudWidget.canvas.draw()

        self.wordlistWidget.display_wordlist(word_dict)

from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLabel, QComboBox, QTableWidget, QTableWidgetItem
#感情分
from emtionPart import test_jd
class EmotionScore(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        self.setWindowTitle("选择商品界面")
        self.setGeometry(200, 200, 1000, 1024)

        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(4)  # Changed to 3 columns
        self.tableWidget.setHorizontalHeaderLabels(["评论内容", "snowNLP感情分", "分词感情分","是否保留"])
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

    def load_data(self, data):
        self.tableWidget.setRowCount(len(data))
        for row, rowData in enumerate(data):
            for col, value in enumerate(rowData):
                item = QTableWidgetItem(str(value))
                self.tableWidget.setItem(row, col, item)

    def clear_layout(self):
        for i in reversed(range(self.layout().count())):
            widget = self.layout().itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    # def run(self):


# class bigmodel(QWidget):

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = SearchableComboBoxWidget()
    widget.show()
    sys.exit(app.exec_())

    # app = QApplication(sys.argv)
    # worldcloud = WordCloudDialog("100084057740")
    # worldcloud.show()
    # sys.exit(app.exec_())




    # test
    # wordCloud = wordCloud()
    # wordCloud.draw(ID)
    # lda = LDA()
    # lda.run("100006390453")
    # lda.openHTML("100006390453")


    # def read_csv(filename):
    #     data = []
    #     with open(filename, newline='', encoding='utf-8') as csvfile:
    #         reader = csv.reader(csvfile)
    #         for row in reader:
    #             data.append(row)
    #     return data
    #
    # app = QApplication(sys.argv)
    # emotion = EmotionScore()
    # ID = 100006390453
    # filename = f'{ID}.csv'
    # directory = "emotionScore"
    # file_path = os.path.join(directory, filename)
    # data = data = read_csv(file_path)
    # emotion.load_data(data)
    # emotion.exec_()
    # sys.exit(app.exec_())
    # from suggestionPart import TextDialog
    # widget = TextDialog("100006390453")
    # widget.show()
    # sys.exit(app.exec_())