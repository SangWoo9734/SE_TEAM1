import requests
from bs4 import BeautifulSoup
import csv

# 서울특별시 - 내 손안에 서울
# 페이지에서 검색 crawling 이용은 어려움
# basic_url = 'https://mediahub.seoul.go.kr/search/searchDetailList.do'
# 실제 기사 url
web = ['https://mediahub.seoul.go.kr/archives/2001287', 'https://mediahub.seoul.go.kr/archives/2001152', 'https://mediahub.seoul.go.kr/archives/2000380']

f = open('src.csv', 'w',  encoding='utf-8-sig', newline='')
wr = csv.writer(f)

# call html
response = requests.post(web[0])
html = response.text
soup = BeautifulSoup(html, 'html.parser')
title = ""
content = ""
imgUrl = ""

for tag in soup.select('#fontScaleTarget > div.news_detail_view > div > div.boxing > h3'):
    title = tag.get_text()
for tag in soup.select('#fontScaleTarget > div.cont_aside > div.cont > div > div.news_detail_cont > div:nth-child(1) > div > div'):
    content = tag.get_text()
for tag in soup.select('#fontScaleTarget > div.cont_aside > div.cont > div > div.news_detail_cont > div:nth-child(2) > div > div.img > img'):
    imgUrl = tag['src']

wr.writerow([1, title, content, imgUrl])

response = requests.post(web[1])
html = response.text
soup = BeautifulSoup(html, 'html.parser')
title = ""
content = ""
imgUrl = ""

for tag in soup.select('#fontScaleTarget > div.news_detail_view > div > div.boxing > h3'):
    title = tag.get_text()
for tag in soup.select('#fontScaleTarget > div.cont_aside > div.cont > div > div.news_detail_cont > div:nth-child(2) > div > div'):
    content = tag.get_text()
for tag in soup.select('#fontScaleTarget > div.cont_aside > div.cont > div > div.news_detail_cont > div:nth-child(3) > div > div.img > img'):
    imgUrl = tag['src']

wr.writerow([2, title, content, imgUrl])

response = requests.post(web[2])
html = response.text
soup = BeautifulSoup(html, 'html.parser')
title = ""
content = ""
imgUrl = ""

for tag in soup.select('#fontScaleTarget > div.news_detail_view > div > div.boxing > h3'):
    title = tag.get_text()
for tag in soup.select('#fontScaleTarget > div.cont_aside > div.cont > div > div.news_detail_cont > div:nth-child(1) > div > div'):
    content = tag.get_text()
for tag in soup.select('#fontScaleTarget > div.cont_aside > div.cont > div > div.news_detail_cont > div:nth-child(2) > div > div.img > img'):
    imgUrl = tag['src']

wr.writerow([3, title, content, imgUrl])

f.close()
