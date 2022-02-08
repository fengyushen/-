# 作答区域1：请求网页，可以尝试将网址替换为B站视频排行榜哦！
# 作答区域2：查找soup中所有class属性值为title的a标签
# 作答区域3：打印标签的文字内容
import requests
import bs4
#url = "https://static0.xesimg.com/pythonweb/编程八卦/index.html"
# # B站热门视频排行榜
url = "https://www.bilibili.com/v/popular/rank/all"
#作答区域1：补充下一行代码，请求网页
res = requests.get(url)
res.encoding = "UTF-8"
soup = bs4.BeautifulSoup(res.text, "lxml")
#作答区域2：补充下一行代码，选取标签名为a，class属性值为title的标签
data = soup.find_all("a",class_="title")
for n in data:
    #作答区域3：补充下一行代码，打印标签的文字内容
    print(n.text)
