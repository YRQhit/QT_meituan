from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar
from PyQt5.QtCore import QTimer


class CountdownWindow(QWidget):
    def __init__(self, duration):
        super().__init__()
        self.setWindowTitle("Countdown Window")
        self.setGeometry(200, 200, 300, 100)

        self.duration = duration
        self.remaining_time = 0  # 从0开始计数

        self.setupUi()

    def setupUi(self):
        layout = QVBoxLayout()

        # Add progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(self.duration)
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)

        # Start countdown timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every second

    def update_time(self):
        self.remaining_time += 1  # 每秒加1
        if self.remaining_time <= self.duration:
            self.progress_bar.setValue(self.remaining_time)
        else:
            self.timer.stop()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = CountdownWindow(60)  # 60秒的倒计时
    window.show()
    sys.exit(app.exec_())
