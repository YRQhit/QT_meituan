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

#任务完成窗口
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

#任务爬取窗口
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
    def __init__(self, ID):
        self.ID = ID
        self.productId = 'productId=' + ID
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

    def run(self):
        global list_comment
        #productId= + num
        ID = self.productId
        if os.path.exists('comments/' + str(ID) + '.csv'):
            print("之前下载过")
            # dialog = TaskCompleteDialog()
            # dialog.exec_()
        else:
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

            productid = ID
            # for proc in productid:  # 遍历产品颜色
            proc = self.productId
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
            # dialog = TaskCompleteDialog()
            # dialog.exec_()

class GetBaseinformation():
    def __init__(self, ID):
        self.ID = ID

    def run(self):
        ua = UserAgent()
        format_url = 'https://item.jd.com/{0}.html'
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

        # ID = "10043284693417"
        url = format_url.format(self.ID)

        # url = "https://item.jd.com/100060887464.html"
        try:
            response = requests.get(url=url, headers=headers, verify=False)
            jsonData = response.text
            print(jsonData)
        except:
            print("error")

    def get_page(self):
        page_list = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                            (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
        }  # 定义头部



        url = "https://item.jd.com/{}.html".format(self.ID)
        page = requests.get(url, headers=headers)
        print("页面状态码:{0}".format( page.status_code))
        time.sleep(1.5)  # 程序挂起, 防止反爬虫
        # page = requests.get()
        # page_list.append(page)

        return page
    def analysis_page(self, analysis):

        soup = BeautifulSoup(analysis.text, "html.parser")
        # print(soup)
        print("----------")
        div = soup.find_all('div', attrs={"class": ['Ptable-item']})  # 返回div为列表
        # print(div)
        # print("-----------")
        li = soup.find_all('ul', attrs={"class": ['parameter2 p-parameter-list']})  # 返回div为列表
        # print(li)
        # print("-----------")
        # 查找所有的 <li> 标签
        data = []
        # itemName = li[0].find_all('li')[0].get('title')
        # itemId = li[0].find_all('li')[1].get('title')
        # itemWeight= li[0].find_all('li')[2].get('title')
        # itemOrigin = li[0].find_all('li')[3].get('title')
        # itemHeat = li[0].find_all('li')[4].get('title')
        # itemStorage = li[0].find_all('li')[5].get('title')

        itemName = li[0].find_all('li')[0].text.strip()
        itemInformation = ""

        for item in range(len(li[0].find_all('li'))):
            if "商品名称" in li[0].find_all('li')[item].text.strip():
                itemName = li[0].find_all('li')[item].text.strip()
            elif "商品编号" in li[0].find_all('li')[item].text.strip():
                itemId = li[0].find_all('li')[item].text.strip()
            # elif "包装形式" in li[0].find_all('li')[item].text.strip():
            #     itemPack = li[0].find_all('li')[item].text.strip()
            # elif "食用方法" in li[0].find_all('li')[item].text.strip():
            #     itemHeat = li[0].find_all('li')[item].text.strip()
            # elif "国产/进口" in li[0].find_all('li')[item].text.strip():
            #     itemOrigin = li[0].find_all('li')[item].text.strip()
            # elif "贮存条件" in li[0].find_all('li')[item].text.strip():
            #     itemStorage = li[0].find_all('li')[item].text.strip()
            # elif "口味" in li[0].find_all('li')[item].text.strip():
            #     itemTaste = li[0].find_all('li')[item].text.strip()
            else:
                itemInformation = itemInformation +","+ li[0].find_all('li')[item].text.strip()
        # print(itemName,itemId,itemWeight,itemOrigin,itemHeat)
        returnValue = itemName + "\n" + itemId + "\n" + itemInformation
        imgPath = "https:" + soup.find('div', id='main-img-{}'.format(self.ID)).find('img').get('data-origin')
        # print(imgPath)
        #图片下载
        filename = f"{itemId}.jpg"
        directory = "Picture"
        PicPath = os.path.join(directory, filename)
        if os.path.exists(PicPath):
            print("图片已被下载")
        else:
            self.download_image(imgPath, self.ID)

        data.append([itemName, itemId, itemInformation, imgPath])

        file_path = "Commodity/"+ "jd.csv"
        with open(file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)
            print("图片下载完毕")
        return returnValue

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


if __name__ == "__main__":
    # comment = commentSpider()
    # comment.run()
    ID = "100060887464"
    information = GetBaseinformation(ID)
    information.analysis_page(information.get_page())
    # comment = commentSpider(ID)
    # comment.run()