from bs4 import BeautifulSoup

html = """
<ul class="parameter2 p-parameter-list">
<li title="灵略金汤酸菜鱼450g*3袋">商品名称：灵略金汤酸菜鱼450g*3袋</li>
<li class="shieldShopInfo" title="100060887464">商品编号：100060887464</li>
<li title="1.44kg">商品毛重：1.44kg</li>
<li title="中国大陆">商品产地：中国大陆</li>
<li title="袋装">包装形式：袋装</li>
<li title="加热即食，再烹饪">食用方法：加热即食，再烹饪</li>
<li title="冷冻">贮存条件：冷冻</li>
</ul>
"""

# 创建 BeautifulSoup 对象
soup = BeautifulSoup(html, 'html.parser')

# 查找所有的 <li> 标签
li_tags = soup.find_all('li')

# 遍历每个 <li> 标签，提取商品信息
for li in li_tags:
    title = li.get('title')  # 获取 title 属性值
    text = li.text.split('：')[-1]  # 获取标签文本内容，并截取冒号后面的部分
    print(title, text)
