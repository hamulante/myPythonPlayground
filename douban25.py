import requests
from bs4 import BeautifulSoup # pip install requests beautifulsoup4 done
import time

#第一页https://movie.douban.com/top250 or https://movie.douban.com/top250?start=0&filter=
#https://movie.douban.com/top250?start=225&filter=
#网页会从第226个开始显示,显示25个
#没有规定的话，默认就是平均分25个/页




def getmovies(url):
    #缺少头部的话，豆瓣不认为是一个浏览器请求，会直接返回空界面
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'
    }#实际的浏览器抄下来的
    response = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(response.text,'html.parser')
    movie_items = soup.find_all('div',class_='item')

    #print(movie_items)

    for item in movie_items:
        rank = item.find('em').text
        name = item.find('span',class_="title").text
        print(rank,name)

    return

if __name__=="__main__":
    url='https://movie.douban.com/top250'
    getmovies(url)
