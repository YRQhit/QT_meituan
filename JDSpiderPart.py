import json
import csv
import sys
import time
import random
import tkinter
from selenium import webdriver
from selenium.webdriver.common.by import By
from threading import Thread
from playsound import playsound
import functions.jdSpiderDependence as jds
import requests
import os
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLabel, QComboBox, QTableWidget, QTableWidgetItem
from enum import Flag
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time
import numpy as np
import requests
import json
import csv
import io
VERSION='1.0'
# print(f'程序版本{VERSION}\n最新程序下载地址:https://github.com/zhangjiancong/MarketSpider')
# 全局变量状态文字
gui_text = {}
gui_label_now = {}
gui_label_eta = {}
# from threading import Thread
from PyQt5.QtCore import pyqtSignal, QObject

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar
from PyQt5.QtCore import QTimer





class TaskCompleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task completed")
        self.setupUi()

    def setupUi(self):
        layout = QVBoxLayout()

        label = QLabel("下载完毕")
        layout.addWidget(label)

        button = QPushButton("OK")
        button.clicked.connect(self.accept)  # Close the dialog when OK button is clicked
        layout.addWidget(button)

        self.setLayout(layout)

class TaskStartDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Start")
        self.setupUi()

    def setupUi(self):
        layout = QVBoxLayout()

        label = QLabel("下载开始")
        layout.addWidget(label)

        button = QPushButton("OK")
        button.clicked.connect(self.accept)  # Close the dialog when OK button is clicked
        layout.addWidget(button)

        self.setLayout(layout)

class SpiderDialog(QDialog):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setWindowTitle("爬虫")
        self.setGeometry(200, 200, 300, 300)  # Set window position (x, y) and size (width, height)

        # 创建两个按钮，分别连接到不同的槽函数
        self.button1 = QPushButton("爬取商品信息")
        self.button1.clicked.connect(self.open_sub_dialog1)
        layout.addWidget(self.button1)

        self.button2 = QPushButton("爬取评论信息")
        self.button2.clicked.connect(self.open_sub_dialog2)
        layout.addWidget(self.button2)

        self.setLayout(layout)

    def open_sub_dialog1(self):
        sub_dialog = JDSpiderWindow()
        sub_dialog.run()

    def open_sub_dialog2(self):
        sub_dialog = CommiteSpider()
        sub_dialog.exec_()

class JDSpiderWindow():
    #判断变量没有定义
    def is_variable_defined(self, var_name):
        global_var_dict = globals()
        return var_name in global_var_dict

    #得到输入框的字符串
    def on_submit(self):
        global keyword
        keyword = entry.get()
        print("You entered:", keyword)
        gui_text['text'] = '☞等待搜索关键词'
        # 在这里添加启动浏览器的代码

    #删除提示
    def on_entry_click(self, event):
        if entry.get() == '请输入关键词':
            entry.delete(0, tkinter.END)
            entry.config(fg='black')  # 设置文本颜色为黑色

    #提示输入关键词
    def on_focusout(self, event):
        if entry.get() == '':
            entry.insert(0, '请输入关键词')
            entry.config(fg='grey')  # 设置文本颜色为灰色


    def download_image(self, url, filename):
        from PIL import Image
        import pillow_avif
        send_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
            "Connection": "keep-alive",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8"}

        response = requests.get(url, headers=send_headers)
        if response.status_code == 200:
            # 写入文件
            filename = f"{filename}.avif"
            directory = "Picture"
            PicPath = os.path.join(directory, filename)
            with open(PicPath, 'wb') as f:
                f.write(response.content)
            print("图片下载成功")
            AVIFfilename = PicPath
            AVIFimg = Image.open(AVIFfilename)
            AVIFimg.save(AVIFfilename.replace("avif", 'jpg'), 'JPEG')
        else:
            print("下载失败，HTTP 状态码:", response.status_code)

        # try:
        #     # 发送 HTTP GET 请求获取图片内容
        #     response = requests.get(url, headers=send_headers)
        #     if response.status_code == 200:
        #
        #         # 写入文件
        #         filename = f"{filename}.jpg"
        #         directory = "Picture"
        #         PicPath = os.path.join(directory, filename)
        #         with open(PicPath, 'wb') as f:
        #             f.write(response.content)
        #         print("图片下载成功")
        #     else:
        #         print("下载失败，HTTP 状态码:", response.status_code)
        #
        # except Exception as e:
        #     print("下载失败:", str(e))

    #判断按钮有没有按下
    def check_button_click(self):
        global button_clicked
        if not button_clicked:
            print("按钮未被按下，暂停...")
            # 在这里可以执行暂停操作
        else:
            print("按钮已被按下")
            # 在这里可以执行相应的操作
    # GUI函数
    def guiFunc(self):
        global entry
        global gui_text
        global gui_label_now
        global gui_label_eta
        global keyword
        gui = tkinter.Tk()
        gui.title('京东店铺信息爬取器')
        gui['background'] = '#eeeeee'
        gui.geometry("600x180-50+20")
        gui.attributes("-topmost", 1)
        gui_text = tkinter.Label(gui, text='初始化', font=('微软雅黑', '20'))
        gui_text.pack()
        entry = tkinter.Entry(gui, width=30)

        default_text = '请输入关键词'
        entry.insert(0, default_text)
        entry.bind("<FocusIn>", self.on_entry_click)
        entry.bind("<FocusOut>", self.on_focusout)

        entry.pack(pady=10)
        # entry.pack(pady=10)

        submit_btn = tkinter.Button(gui, text="提交", command=self.on_submit)
        submit_btn.pack()

        # check_button_click_btn = tkinter.Button(gui, text="检查按钮是否按下", command=check_button_click)
        # check_button_click_btn.pack()

        submit_btn.pack()
        gui_label_now = tkinter.Label(gui, text='?', font=('微软雅黑', '10'))
        gui_label_now.pack()
        gui_label_eta = tkinter.Label(gui, text='?', font=('微软雅黑', '10'))
        gui_label_eta.pack()
        gui.mainloop()



    def run(self):

        # GUI线程控制
        Gui_thread = Thread(target=self.guiFunc, daemon=True)
        Gui_thread.start()
        time.sleep(2)

        # 启动浏览器
        gui_text['text'] = '☞等待搜索关键词'

        # keyword = input('输入搜索关键词:')
        while not self.is_variable_defined('keyword'):
            # print("my_variable 未定义")
            time.sleep(1)
            pass

        gui_text['text'] = '正在启动浏览器'
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        browser = webdriver.Chrome(options=options)
        browser.get('https://www.jd.com')

        # CSV相关
        import os
        # csvPath = f'{keyword}-jd-{time.strftime("%Y%m%d%H%M", time.localtime())}.csv'
        csvPath = f'{keyword}-jd.csv'
        directory = "Commodity"
        file_path = os.path.join(directory, csvPath)
        csvfile = open(file_path, 'a', encoding='utf-8-sig',
                       newline='')
        csvWriter = csv.DictWriter(csvfile,
                                   fieldnames=['item_name', 'item_price', 'item_shop', 'shop_link', 'item_link', 'jdshop_id','item_id','item_commit_number','itemURL'])

        # cookie相关
        gui_text['text'] = '正在清空Cookie'
        browser.delete_all_cookies()
        gui_text['text'] = '正在注入Cookie'

        directory = "Cookie"
        filename = "jd.cookie"
        CookiePath = os.path.join(directory, filename)
        try:
            with open(CookiePath, 'r') as f:
                cookie_list = json.load(f)
                for cookie in cookie_list:
                    browser.add_cookie(cookie)
        except:
            print('未找到Cookie')
        gui_text['text'] = '正在刷新浏览器'
        browser.refresh()

        # 搜索词与页数获取
        gui_text['text'] = '正在操作'
        browser.find_element(By.ID, 'key').send_keys(keyword)
        browser.find_element(By.CLASS_NAME, 'button').click()
        time.sleep(10)
        ##J_filter > div.f-line.top > div.f-sort > a:nth-child(2) > span
        ##J_filter > div.f-line.top > div.f-sort > a:nth-child(2)
        ##J_filter > div.f-line.top > div.f-sort > a:nth-child(2)
        # browser.find_element(By.CLASS_NAME, 'onclick').click()
        browser.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div[1]/a[2]').click()
        browser.implicitly_wait(10)
        jdPage = browser.find_element(By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > em:nth-child(1) > b').text
        browser.execute_script("document.documentElement.scrollTop=100000")

        # 爬取页数控制
        gui_text['text'] = '☞等待爬取页数'
        print(f'共计{jdPage}页，建议每2小时总计爬取不超过20页')


        # page_start = int(input('起始页数：'))
        # page_end = int(input('截止页数：')) + 1

        #默认参数
        page_start = 1
        page_end = 2

        for page in range(page_start, page_end):
            gui_text['text'] = f'当前正在获取第{page}页，还有{page_end - page_start - page}页'
            gui_text['bg'] = '#10d269'
            gui_label_now['text'] = '-'
            gui_label_eta['text'] = '-'
            browser.execute_script(f"SEARCH.page({2 * page - 1}, true)")
            time.sleep(5)
            browser.execute_script("document.documentElement.scrollTop=100000")
            time.sleep(2)
            browser.execute_script("document.documentElement.scrollTop=9959")
            # 每一页有60项
            for i in range(1, 61):
                try:
                    gui_label_now['text'] = f'正在获取：当前页第{i}个，剩余{60 - i}个'
                    item_name = browser.find_element(By.CSS_SELECTOR,
                                                     f'#J_goodsList > ul > li:nth-child({i}) > div > div.p-name.p-name-type-2 > a > em').text
                    #/html/body/div[5]/div[2]/div[2]/div[2]/div/div[1]/div[2]/ul/li[1]/div[2]/strong/i
                    #document.querySelector("#ad-291-10061014997678 > div.p-price > strong > i")
                    item_price = browser.find_element(By.CSS_SELECTOR,
                                                      f'#J_goodsList > ul > li:nth-child({i}) > div > div.p-price > strong > i').text
                    item_shop = browser.find_element(By.CSS_SELECTOR,
                                                     f'#J_goodsList > ul > li:nth-child({i}) > div > div.p-shop > span > a').text
                    shop_link = browser.find_element(By.CSS_SELECTOR,
                                                     f'#J_goodsList > ul > li:nth-child({i}) > div > div.p-shop > span > a').get_attribute(
                        'href')
                    item_link = browser.find_element(By.CSS_SELECTOR,
                                                     f'#J_goodsList > ul > li:nth-child({i}) > div > div.p-img > a').get_attribute(
                        'href')
                    jdshop_id = jds.shop_id_get(shop_link)
                    item_id = browser.find_element(By.CSS_SELECTOR,
                                                   f'#J_goodsList > ul > li:nth-child({i})').get_attribute(
                        'data-sku')
                    ##J_comment_10061014997678
                    item_commit_number = browser.find_element(By.CSS_SELECTOR,
                                                       f'#J_goodsList > ul > li:nth-child({i}) > div > div.p-commit > strong > a').text

                    ##J_goodsList > ul > li:nth-child(30) > div > div.p-img > a > img
                    ##J_goodsList > ul > li:nth-child(9) > div > div.p-img > a > img
                    ##J_goodsList > ul > li:nth-child(14) > div > div.p-img > a > img
                    #商品图片url
                    itemURL = ""
                    while itemURL == "":
                        # time.sleep(2)
                        itemURL = browser.find_element(By.CSS_SELECTOR,f'#J_goodsList > ul > li:nth-child({i}) > div > div.p-img > a > img').get_attribute('src')
                        try:
                            print(itemURL)
                            self.download_image(itemURL, item_id)
                        except:
                            itemURL = ""
                            time.sleep(15)
                            # print(itemURL)
                            pass

                    csvWriter.writerow(
                        {'item_name': item_name, 'item_price': item_price, 'item_shop': item_shop, 'shop_link': shop_link,
                         'item_link': item_link, 'jdshop_id': jdshop_id,'item_id':item_id,'item_commit_number':item_commit_number,'itemURL':itemURL})
                    csvfile.flush()


                except:
                    gui_text['text'] = f'出错：如有验证请验证。等待10秒'
                    gui_text['bg'] = 'red'
                    gui_label_eta['text'] = '-'
                    gui_label_now['text'] = '-'
                    playsound('error.wav')
                    time.sleep(10)
            delay_time = random.randint(10, 30)
            for delay in range(delay_time):
                gui_label_now['text'] = '-'
                gui_text['bg'] = '#eeeeee'
                gui_label_eta['text'] = f'延时翻页：已延时{delay}秒，总共延时{delay_time}秒'
                time.sleep(1)

        print('程序结束')
        gui_text['text'] = '程序结束正在保存文件'
        csvfile.close()
        gui_text['text'] = '保存文件完成，准备退出中'
        time.sleep(5)
        browser.close()
        dialog = TaskCompleteDialog()
        dialog.exec_()
        # sys.exit()


class CommiteSpider(QDialog):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setWindowTitle("选择商品界面")
        self.setGeometry(200, 200, 1000, 1024)
        # 创建下拉框
        self.comboBox = QComboBox()
        self.comboBox.addItem("按照名称排序")
        self.comboBox.addItem("按照价格排序")
        self.comboBox.addItem("按照超市排序")
        self.comboBox.addItem("按照ID排序")
        self.comboBox.currentIndexChanged.connect(self.sort_data)  # 连接下拉框选项变更信号到排序槽函数
        layout.addWidget(self.comboBox)

        # 创建表格
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["商品名称", "商品价格", "商品超市", "商品ID"])

        self.data = self.loadCsv()

        self.update_table()  # 初始化表格显示

        self.tableWidget.setRowCount(len(self.data))


        layout.addWidget(self.tableWidget)

        # 创建按钮
        self.button = QPushButton("获取选中的元素")
        self.button.clicked.connect(self.get_selected_items)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def get_selected_items(self):
        dialog = TaskStartDialog()
        dialog.exec_()
        selected_items = self.tableWidget.selectedItems()
        if selected_items:
            selected_text =  ['productId='+item.text() for item in selected_items]

            a = commentSpider()
            a.run(selected_text)
            
            print("选中的元素:", selected_text)
        else:
            print("未选中任何元素")
    #加载Csv文件
    def loadCsv(self):
        import os
        keyword = "预制菜"
        filename = f'{keyword}-jd.csv'
        directory = "Commodity"
        file_path = os.path.join(directory, filename)
        #'item_name', 'item_price', 'item_shop', 'shop_link', 'item_link', 'jdshop_id','item_id','item_commit_number','itemURL'
        columns = [0, 1, 2, 6]
        data = []
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                # 仅提取指定列的数据
                selected_columns = [row[col] for col in columns]
                # selected_columns = [float(row[col]) if col in [1] else row[col] for col in columns]
                data.append(selected_columns)
        print(data)
        return data

    #排序
    def sort_data(self, index):
        if index == 0:  # 按照名称
            self.data.sort(key=lambda x: x[0])
        elif index == 1:  # 按照价格
            self.data.sort(key=lambda x: float(x[1]))
        elif index == 2:  # 按照超市
            self.data.sort(key=lambda x: x[2])
        elif index == 3:  # 按照ID排序
            self.data.sort(key=lambda x: float(x[3]))
        self.update_table()  # 更新表格显示


    #表格更新
    def update_table(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(self.data))
        for row, row_data in enumerate(self.data):
            for col, col_data in enumerate(row_data):
                item = QTableWidgetItem(col_data)
                self.tableWidget.setItem(row, col, item)


class commentSpider():
    # -*- encoding: utf-8 -*-
    from enum import Flag
    # from fake_useragent import UserAgent
    from bs4 import BeautifulSoup
    import time
    import numpy as np
    import requests
    import json
    import csv
    import io

    # 保存评论数据

    def commentSave(self, nameid, list_comment):
        '''
        list_comment: 二维list,包含了多条用户评论信息
        '''
        file = io.open('comments/' + str(nameid) + '.csv', 'w', encoding="utf-8", newline='')
        writer = csv.writer(file)
        writer.writerow(['用户ID', '评论内容', '购买时间', '点赞数', '回复数', '得分', '评价时间', '商品'])
        for i in range(len(list_comment)):
            writer.writerow(list_comment[i])
        file.close()
        print('存入成功')

    def getCommentData(self,headers, format_url, proc, i, maxPage):
        '''
        format_url: 格式化的字符串架子，在循环中给它添上参数
        proc: 商品的productID，标识唯一的商品号
        i: 商品的排序方式，例如全部商品、晒图、追评、好评等
        maxPage: 商品的评论最大页数
        '''
        sig_comment = []
        global list_comment
        cur_page = 0
        while cur_page < maxPage:
            cur_page += 1
            # url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv%s&score=%s&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1'%(proc,i,cur_page)
            url = format_url.format(proc, i, cur_page)  # 给字符串添上参数
            try:
                requests.packages.urllib3.disable_warnings()
                response = requests.get(url=url, headers=headers, verify=False)
                time.sleep(np.random.rand() * 2)
                jsonData = response.text
                startLoc = jsonData.find('{')
                # print(jsonData[::-1])//字符串逆序
                jsonData = jsonData[startLoc:-2]
                jsonData = json.loads(jsonData)
                pageLen = len(jsonData['comments'])
                # print("当前第%s页"%cur_page)
                for j in range(0, pageLen):
                    userId = jsonData['comments'][j]['id']  # 用户ID
                    content = jsonData['comments'][j]['content']  # 评论内容
                    boughtTime = jsonData['comments'][j]['referenceTime']  # 购买时间
                    voteCount = jsonData['comments'][j]['usefulVoteCount']  # 点赞数
                    replyCount = jsonData['comments'][j]['replyCount']  # 回复数目
                    starStep = jsonData['comments'][j]['score']  # 得分
                    creationTime = jsonData['comments'][j]['creationTime']  # 评价时间
                    referenceName = jsonData['comments'][j]['referenceName']  # 商品名称

                    sig_comment.append(userId)  # 每一行数据
                    sig_comment.append(content)
                    sig_comment.append(boughtTime)
                    sig_comment.append(voteCount)
                    sig_comment.append(replyCount)
                    sig_comment.append(starStep)
                    sig_comment.append(creationTime)
                    sig_comment.append(referenceName)
                    list_comment.append(sig_comment)
                    # print(sig_comment)
                    sig_comment = []
            except:
                time.sleep(5)
                cur_page -= 1
                print('网络故障或者是网页出现了问题，五秒后重新连接')

    import csv
    def read_csv_column(self, file_path, column_index):
        column_data = []

        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)
            for row in csv_reader:
                if len(row) > column_index:  # 确保指定的列存在于每一行中
                    strlist = 'productId=' + row[column_index]
                    column_data.append(str(strlist))
        return column_data

    def run(self,productid):
        global list_comment
        ua = UserAgent()
        # https://detail.tmall.com/item.htm?ali_refid=a3_430582_1006:1187590015:N:qsEePeNoKpu0oxySW5wwzQ==:10f4e3ff1924e60b00b8275e056b9ecf&ali_trackid=199_10f4e3ff1924e60b00b8275e056b9ecf&id=585154798857&spm=a21n57.1.item.1
        # https://detail.tmall.com/item.htm?ali_refid=a3_430582_1006:1187590015:N:qsEePeNoKpu0oxySW5wwzQ==:10f4e3ff1924e60b00b8275e056b9ecf&ali_trackid=199_10f4e3ff1924e60b00b8275e056b9ecf&id=585154798857&spm=a21n57.1.item.1
        format_url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&{0}&score={1}&sortType=5&page={2}&pageSize=10&isShadowSku=0&fold=1'
        # 设置访问请求头
        headers = {
            'Accept': '*/*',
            'Host': "club.jd.com",
            "User-Agent": ua.random,
            'sec-ch-ua': "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'script',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-site',
        }

        # 手机四种颜色对应的产品id参数
        # file_path = 'Commodity//预制菜-jd.csv'  # 替换为你的 CSV 文件路径
        # column_index = 6  # 替换为你要读取的列的索引，从0开始计数
        #
        # csv_reader = self.read_csv_column(file_path, column_index)
        #
        # productid = csv_reader
        # print(productid)
        # productid = ["10043284693417"]
        sig_comment = []
        for proc in productid:  # 遍历产品颜色
            i = -1
            list_comment = [[]]
            while i < 7:  # 遍历排序方式
                i += 1
                if (i == 6):
                    continue
                # 先访问第0页获取最大页数，再进行循环遍历
                url = format_url.format(proc, i, 0)
                print(url)
                try:
                    response = requests.get(url=url, headers=headers, verify=False)
                    jsonData = response.text
                    # print(jsonData)
                    startLoc = jsonData.find('{')
                    jsonData = jsonData[startLoc:-2]
                    jsonData = json.loads(jsonData)
                    print("最大页数%s" % jsonData['maxPage'])
                    # jsonData['maxPage'] = 3

                    self.getCommentData(headers, format_url, proc, i, jsonData['maxPage'])  # 遍历每一页
                except Exception as e:
                    i -= 1
                    print("the error is ", e)
                    print("wating---")
                    time.sleep(5)

            nameid = proc
            print("爬取结束，开始存储-------")
            self.commentSave(nameid, list_comment)
            dialog = TaskCompleteDialog()
            dialog.exec_()




if __name__ == "__main__":

    # JD = JDSpiderWindow()
    # JD.run()
    #主程序
    app = QApplication(sys.argv)
    main_dialog = SpiderDialog()
    main_dialog.show()
    sys.exit(app.exec_())
    #测试评论部分爬虫
    # comment = commentSpider()
    # comment.run()