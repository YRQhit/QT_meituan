import json
import time


from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLineEdit, QLabel, QPushButton
from PyQt5.QtCore import QThread, pyqtSignal

#倒计时函数
# class CountdownThread(QThread):
#     def __init__(self, window):
#         super().__init__()
#         self.window = window
#
#     def run(self):
#         for delaytime in range(0, 61):
#             self.window.update_text(delaytime)
#             time.sleep(1)

class CountdownThread(QThread):
    progress_updated = pyqtSignal(int)  # 发送倒计时进度的信号

    def __init__(self):
        super().__init__()

    def run(self):
        for delaytime in range(60, -1, -1):
            print(delaytime)
            self.progress_updated.emit(delaytime)
            self.msleep(1000)  # 每隔1秒发送一次信号

#网络并发
class NetworkThread(QThread):
    finished = pyqtSignal()

    def __init__(self):
        super().__init__()

    def run(self):
        # 在这里执行网络请求的代码
        # 例如使用 requests 或者 aiohttp 库
        # 请求完成后发出信号表示完成
        self.finished.emit()

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar
from PyQt5.QtCore import QTimer

#进度条显示
class CountdownWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Countdown Window")
        self.setGeometry(200, 200, 300, 100)

        self.setupUi()

    def setupUi(self):
        layout = QVBoxLayout()

        # Add label to display text
        self.display_label = QLabel()
        layout.addWidget(self.display_label)

        self.setLayout(layout)

    def update_text(self, remaining_time):
        print(remaining_time)
        # self.display_label.setText("123")
        # print(remaining_time)
        self.display_label.setText(f"剩余时间：{remaining_time} 秒")
        # self.display_label.setText("{}".format(remaining_time))
        # print(self.display_label.setText("{}".format(remaining_time)))

from PyQt5.QtCore import QThread, pyqtSignal, QObject, QMetaObject
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QDialog, QPushButton
import sys
from PyQt5.QtCore import Qt
class CookieWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Get Cookie Window")
        self.setGeometry(200, 200, 300, 150)  # Set window position (x, y) and size (width, height)
        self.setupUi()

    def setupUi(self):
        layout = QVBoxLayout()

        # Add label
        label = QLabel("\n输入数字打开网站\n0>淘宝\t1>京东\t2>拼多多(仅支持手机验证码登录)\t3>阿里巴巴1688")
        layout.addWidget(label)

        # Add input field
        self.cookie_input = QLineEdit()
        layout.addWidget(self.cookie_input)

        # Add button
        button = QPushButton("Submit")
        layout.addWidget(button)
        button.clicked.connect(self.submit_cookie)

        self.setLayout(layout)

    def submit_cookie(self):
        self.web = self.cookie_input.text()
        # print("Cookie value submitted:", self.web)
        # print(self.web)
        self.network_thread = NetworkThread()
        self.network_thread.finished.connect(self.get_cookie)
        self.network_thread.start()

    def on_network_finished(self):
        # print("1")
        # self.get_cookie()
        QMetaObject.invokeMethod(self, "get_cookie", Qt.QueuedConnection)

    def get_cookie(self):
        # print("2")
        # cookie = GetCookiePart()
        # cookie.show()
        # cookie.run()
        cookie = GetCookiePart(int(self.web))
        # self.label.setText(f"Cookie: {cookie}")
        # self.accept()

class TaskCompleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task completed")
        self.setupUi()

    def setupUi(self):
        layout = QVBoxLayout()

        label = QLabel("cookie 成功获得")
        layout.addWidget(label)

        button = QPushButton("OK")
        button.clicked.connect(self.accept)  # Close the dialog when OK button is clicked
        layout.addWidget(button)

        self.setLayout(layout)

import os

# class GetCookiePart(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Countdown Window")
#         self.setGeometry(200, 200, 300, 100)
#
#         self.setupUi()
#
#     def setupUi(self):
#         layout = QVBoxLayout()
#
#         # Add label to display text
#         self.display_label = QLabel()
#         layout.addWidget(self.display_label)
#
#         self.setLayout(layout)
#
#     def update_text(self, remaining_time):
#         print(remaining_time)
#         # self.display_label.setText("123")
#         # print(remaining_time)
#         self.display_label.setText(f"剩余时间：{remaining_time} 秒")
#         # self.display_label.setText("{}".format(remaining_time))
#         # print(self.display_label.setText("{}".format(remaining_time)))
#
#     def run(self):
#         # window = CountdownWindow()
#         # window.show()
#         # window.update_text("123")
#         # sys.exit(app.exec_())
#         countdown_thread = CountdownThread()
#         countdown_thread.progress_updated.connect(self.update_text)
#         countdown_thread.start()
#         countdown_thread.wait()  # Wait for the countdown thread to finish before proceeding
#         # sys.exit(app.exec_())

# def GetCookiePart(user):
#     window = CountdownWindow()
#     window.show()
#     # window.update_text("123")
#     # sys.exit(app.exec_())
#     countdown_thread = CountdownThread()
#     countdown_thread.progress_updated.connect(window.update_text)
#     countdown_thread.start()
#     countdown_thread.wait()  # Wait for the countdown thread to finish before proceeding
#     sys.exit(app.exec_())

def GetCookiePart(user):

    VERSION = '1.1'
    print(f'程序版本{VERSION}\n最新程序下载地址:https://github.com/zhangjiancong/MarketSpider')
    url = ['https://login.taobao.com/member/login.jhtml?redirectURL=http%3A%2F%2Fwww.taobao.com%2F',
           'https://www.jd.com', 'https://mobile.yangkeduo.com/login.html',
           'https://login.taobao.com/?redirect_url=https%3A%2F%2Flogin.1688.com%2Fmember%2Fjump.htm%3Ftarget%3Dhttps%253A%252F%252Flogin.1688.com%252Fmember%252FmarketSigninJump.htm%253FDone%253Dhttps%25253A%25252F%25252Fwww.1688.com%25252F%25253Fspm%25253Da26352.13672862.pcnewalibar.d5.1fa67c26MSitx3&style=tao_custom&from=1688web']
    filename = ['taobao', 'jd', 'pinduoduo', '1688']
    print(
        '操作流程:\n1-选择需要获取cookie的网站\n2-在弹出的窗口中手动操作进行登录\n3-登陆成功后无需操作，等待cookie自动保存')
    print('\n输入数字打开网站\n0>淘宝\t1>京东\t2>拼多多(仅支持手机验证码登录)\t3>阿里巴巴1688')

    print('请在稍后打开的窗口中登录,限时60秒')
    time.sleep(3)
    from selenium import webdriver
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.get(url[user])
    print('请登录，请在60秒内完成！')


    # app = QApplication(sys.argv)
    # window = CountdownWindow()
    # window.show()
    # # window.update_text("123")
    # # sys.exit(app.exec_())
    # countdown_thread = CountdownThread()
    # countdown_thread.progress_updated.connect(window.update_text)
    # countdown_thread.start()
    # countdown_thread.wait()  # Wait for the countdown thread to finish before proceeding
    # sys.exit(app.exec_())

    for delaytime in range(0, 61):
        print(f'\r已等待:{delaytime}\t eta:{60 - delaytime}', end="", flush=True)
        # window.update_text(f'\r已等待:{delaytime}\t eta:{60 - delaytime}')
        time.sleep(1)



    filename = f"{filename[user]}.cookie"
    directory = "Cookie"
    file_path = os.path.join(directory, filename)
    with open(file_path, 'w') as file:
        if user == 0:
            file.write(json.dumps(driver.get_cookies()))
        if user != 0:
            file.write(json.dumps(driver.get_cookies()))
    driver.close()
    driver.quit()

    print('\nCookie已保存')
    dialog = TaskCompleteDialog()
    dialog.exec_()
    time.sleep(5)



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    dialog = CookieWindow()
    dialog.show()
    #最终窗口
    sys.exit(app.exec_())

    # import sys
    # app = QApplication(sys.argv)
    # window = CountdownWindow()
    # window.show()
    # window.update_text("123")
    # sys.exit(app.exec_())
    #
    # # 示例：通过按钮点击更新窗口中的文本
    # def update_window_text():
    #     window.update_text("新的文本")
    #
    # button = QPushButton("更新窗口文本")
    # button.clicked.connect(update_window_text)
    # button.show()
    #
    # sys.exit(app.exec_())

    # app = QApplication(sys.argv)
    # window = CountdownWindow()
    # window.show()
    #
    # countdown_thread = CountdownThread()
    # countdown_thread.progress_updated.connect(window.update_text)
    # countdown_thread.start()
    #
    # sys.exit(app.exec_())