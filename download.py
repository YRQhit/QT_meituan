import os
filepath = os.path.join("Commodity", "预制菜.csv")
# 得到我们浏览历史数据

def read_csv(filename):
    import csv
    data = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

itemID = []
price = []
Totledata = read_csv(filepath)
for item in Totledata:
    itemID.append(item[6])
    price.append(item[1])
# print(itemID)

from fake_useragent import UserAgent
import csv
import requests
from bs4 import BeautifulSoup
import time
class getFullInformation():
    def __init__(self, ID, price):
        self.ID = ID
        self.price = price

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

        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
        ]
        import random
        # headers = {"user-agent:" + random.choice(user_agents)}  # 定义头部

        # print(headers)
        headers = {
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
                          'User-Agent': random.choice(user_agents)
        }  # 定义头部

        # ua = UserAgent()
        # # 设置访问请求头
        # headers = {
        #     'Accept': '*/*',
        #     'Host': "club.jd.com",
        #     "User-Agent": ua.random,
        #     'sec-ch-ua': "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
        #     'sec-ch-ua-mobile': '?0',
        #     'Sec-Fetch-Dest': 'script',
        #     'Sec-Fetch-Mode': 'no-cors',
        #     'Sec-Fetch-Site': 'same-site',
        # }

        url = "https://item.jd.com/{}.html".format(self.ID)
        page = requests.get(url, headers=headers)
        print("页面状态码:{0}".format(page.status_code))
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
                itemInformation = itemInformation + "," + li[0].find_all('li')[item].text.strip()
        # print(itemName,itemId,itemWeight,itemOrigin,itemHeat)
        returnValue = itemName + "\n" + itemId + "\n" + itemInformation
        imgPath = "https:" + soup.find('div', id='main-img-{}'.format(self.ID)).find('img').get('data-origin')
        # print(imgPath)
        # 图片下载
        # filename = f"{itemId}.jpg"
        # directory = "Picture"
        # PicPath = os.path.join(directory, filename)
        # if os.path.exists(PicPath):
        #     print("图片已被下载")
        # else:
        #     self.download_image(imgPath, self.ID)

        data.append([itemName, itemId, itemInformation, imgPath, self.price])

        file_path = "Commodity/" + "jd.csv"
        with open(file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)

        return returnValue

import threading
# 创建一个线程列表
threads = []
# i = 0
# getinformation = getFullInformation(itemID[i], price[i])
# getinformation.analysis_page(getinformation.get_page())

for i in range(196,len(itemID)):
    try:
        getinformation = getFullInformation(itemID[i], price[i])
        getinformation.analysis_page(getinformation.get_page())
    except:
        print(itemID[i])
        pass

# for i in range(len(itemID)):
#     try:
#         getinformation = getFullInformation(itemID[i], price[i])
#         thread = threading.Thread(target=getinformation.analysis_page(getinformation.get_page()), args=(i,))
#         thread.start()
#         threads.append(thread)
#     except:
#         print(itemID[i])
#         pass

# 等待所有线程执行完成
# for thread in threads:
#     thread.join()

print("下载完毕")