#测试Qt中嵌入Matplotlib
import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QWidget, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)

    def plot(self):
        ax = self.figure.add_subplot(111)
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        ax.plot(x, y)
        ax.set_title('Sine Wave')
        self.canvas.draw()

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Matplotlib in QDialog")

        self.matplotlibWidget = MatplotlibWidget()
        self.matplotlibWidget.plot()

        self.button = QPushButton("Close")
        self.button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.matplotlibWidget)
        layout.addWidget(self.button)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())
