import sys
import cv2
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

class ImageDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Image and Histogram')
        self.layout = QVBoxLayout(self)
        self.button = QPushButton('显示图像和RGB曲线', self)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.show_image_and_histogram)
        self.dialog = QDialog()

    def show_image_and_histogram(self,ID):
        # 读取图像
        image = cv2.imread('./Picture/{}.jpg'.format(ID))

        # 将图像拆分成 RGB 通道
        r_channel = image[:,:,2]
        g_channel = image[:,:,1]
        b_channel = image[:,:,0]

        # 计算每个通道的直方图
        hist_r = cv2.calcHist([r_channel], [0], None, [256], [0, 256])
        hist_g = cv2.calcHist([g_channel], [0], None, [256], [0, 256])
        hist_b = cv2.calcHist([b_channel], [0], None, [256], [0, 256])

        # 绘制 RGB 曲线
        plt.plot(hist_r, color='red', label='Red')
        plt.plot(hist_g, color='green', label='Green')
        plt.plot(hist_b, color='blue', label='Blue')
        plt.xlabel('Pixel Intensity')
        plt.ylabel('Frequency')
        plt.title('RGB Histogram')
        plt.legend()
        plt.savefig('histogram\{}.png'.format(ID))

        # 显示原始图像
        image_label = QLabel()
        pixmap = QPixmap('./Picture/{}.jpg'.format(ID))  # 替换为实际的图像路径
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        image_label.setFixedSize(800, 600)

        self.dialog.setWindowTitle('Image and Histogram')
        layout = QHBoxLayout()
        layout.addWidget(image_label)

        histogram_label = QLabel()
        pixmap = QPixmap('histogram\{}.png'.format(ID))
        histogram_label.setPixmap(pixmap)
        histogram_label.setAlignment(Qt.AlignCenter)
        histogram_label.setFixedSize(800, 600)
        layout.addWidget(histogram_label)

        self.dialog.setLayout(layout)
        # self.dialog.resize(800, 600)
        self.dialog.exec_()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageDialog()
    window.show_image_and_histogram("100017594609")
    sys.exit(app.exec_())
