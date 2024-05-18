from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QWidget, QPushButton, QLabel, QScrollArea, QComboBox, QHBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from wordcloud import WordCloud
from collections import Counter
import sys
import os
import jieba
import csv
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
        # self.setStyleSheet("background-color: #ffffff ;")

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
        self.setWindowTitle("词云")
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
        self.setStyleSheet("background-color: #ffffff ;")
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    worldcloud = WordCloudDialog("10099263767130")
    worldcloud.show()
    sys.exit(app.exec_())