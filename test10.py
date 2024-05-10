# 爬取的代码
import requests
import re
import time

goods = '书包'  # 搜索关键字
depth = 2  # 搜索深度为2，即爬取第1页，第2页
# start_url = 'https://search.jd.com/Search?keyword=' + goods + '&enc=utf-8&wq=' + goods
start_url = "https://item.jd.com/100060887464.html"
infoList = []
hd = {'user-agent': 'Mozilla/5.0'}
for j in range(depth):  # 对每一个页面进行处理，使用for循环
    try:
        url = start_url + '&page=' + str(j)  # 组合成带翻页功能的url https://search.jd.com/Search?keyword=书包=utf-8&wq=书包&page=1
        try:
            r = requests.get(url, headers=hd, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding  # 把获取到的页面信息 替换成utf-8信息，这样就不会乱码
            print(r.status_code)
            html = r.text
            print(r.url)
            print(r.text)
        except:
            print("抓取异常")
        try:
            plt = re.findall(r'<em>￥</em><i>.*?\.\d\d', html)  # 获取商品价格,搜索以<em>￥</em><i>开头，以.数字数字结尾的字符串
            tlt = re.findall(r'[^(<em>￥</em>)]<em>.*?[\u4e00-\u9fa5].*?</em>',
                             html)  # 获取商品名称，搜索以<em>开始，以遇到的第一个</em>结尾的字符串,且 第一个字符是(<em>￥</em>)]<em>除外
            for i in range(len(plt)):
                price = plt[i].split('<i>')[1]
                title = tlt[i]
                infoList.append([price, title])  # append() 方法用于在列表末尾添加新的对象。
        except:  # 让程序不会因为异常执行而溢出
            print("分析异常")
    except:
        continue  # 如果某一个页面解析出了entity，那么继续解析下一个页面。
    time.sleep(2)

tplt = "{:^10}\t{:^10}\t{:^20}"  # 设定一个print模板,用大括号{}来定义槽函数
print(tplt.format("序号", "价格",
                  "商品名称"))  # Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。format用法举例：print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
count = 0
for g in infoList:
    count = count + 1
    print(tplt.format(count, g[0], g[1]))  # 打印商品价格、名称，字符串没做处理