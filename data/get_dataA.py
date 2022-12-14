# 要闻传真的获取
import requests #pip install requests
from bs4 import BeautifulSoup #pip install bs4
from fake_useragent import UserAgent  #pip install fake-useragent
import re #模糊匹配

ua = UserAgent() #生成UA

url = 'http://news.sdust.edu.cn/ywcz.htm'
url_auto = 'http://news.sdust.edu.cn/' #补全用的

def get_pages():
  url1='http://news.sdust.edu.cn/ywcz.htm'
  attempt=0
  
  headers={'User-Agent':ua.random} #随机生成UA
  res = requests.get(url1,headers=headers)
  soup = BeautifulSoup(res.text, 'html.parser')
  ans = soup.find('div',class_='pb_sys_common pb_sys_normal pb_sys_style1')#找到页码的class
  # ans2 = ans.find('span',text=re.match("*[/]*"))
  # print(ans2)

def get_top_news():
  headers={'User-Agent':ua.random} #随机生成UA

  res = requests.get(url,headers=headers) #生成headers
  # res.raise_for_status() #test res get
  res.encoding = 'utf-8'
  soup = BeautifulSoup(res.text, 'html.parser')
  ans = soup.find_all('tr',id=re.compile("line_u4_*"))#模糊匹配line_u4_*
  # print(set(ans))
  # ans = set(ans)
  for i in ans:
    # print("-------------------------")
    t = i.find_all('td')
    title = t[0]
    date  = t[1]
    url  = title.a.attrs['href']
    title_str=t[0].text
    date_str=t[1].text
    url_str = str(url)

    # if re.search("http",url_str)==None: #如果没有找到http，自动补全网址
    import urllib
    url_str=urllib.parse.urljoin(url_auto,url_str)

    str1="{title_str} {date_str} {url}".format(title_str=title_str,date_str=date_str,url=url_str)
    print(str1)
    # print("-------------------------")
  # ans = soup.find('tbody')
  # print(ans)

get_pages()