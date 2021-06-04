import requests
from bs4 import BeautifulSoup
import csv

# 서울특별시 - 내 손안에 서울
# get the web url in list
web = ['https://mediahub.seoul.go.kr/archives/1161228', 'https://mediahub.seoul.go.kr/archives/2001152', 'https://mediahub.seoul.go.kr/archives/2000380']

# create file to save the result of crawling
f = open('src.csv', 'w',  encoding='utf-8-sig', newline='')
# write method
wr = csv.writer(f)

# call html
# http request for first web[0]
response = requests.post(web[0])
# get response of request
html = response.text
# BeatifulSoup library for view
soup = BeautifulSoup(html, 'html.parser')
title = ""
content = ""
imgUrl = ""

# get information with tag
for tag in soup.select('#fontScaleTarget > div.news_detail_view > div > div.boxing > h3'):
    title = tag.get_text()
for tag in soup.select('#fontScaleTarget > div.cont_aside > div.cont > div > div.news_detail_cont.oldNews > table > tbody > tr > td'):
    content = tag.get_text()
for tag in soup.select('#fontScaleTarget > div.cont_aside > div.cont > div > div.news_detail_cont.oldNews > p:nth-child(1) > img'):
    imgUrl = tag['src']

# write information to csv file
wr.writerow([title, content, imgUrl])

# call html
# http request for first web[1]
response = requests.post(web[1])
# get response of request
html = response.text
# BeatifulSoup library for view
soup = BeautifulSoup(html, 'html.parser')
title = ""
content = ""
imgUrl = ""

# get information with tag
for tag in soup.select('#fontScaleTarget > div.news_detail_view > div > div.boxing > h3'):
    title = tag.get_text()
for tag in soup.select('#fontScaleTarget > div.cont_aside > div.cont > div > div.news_detail_cont > div:nth-child(2) > div > div'):
    content = tag.get_text()
for tag in soup.select('#fontScaleTarget > div.cont_aside > div.cont > div > div.news_detail_cont > div:nth-child(3) > div > div.img > img'):
    imgUrl = tag['src']

# write information to csv file
wr.writerow([title, content, imgUrl])

# call html
# http request for first web[2]
response = requests.post(web[2])
# get response of request
html = response.text
# BeatifulSoup library for view
soup = BeautifulSoup(html, 'html.parser')
title = ""
content = ""
imgUrl = ""

# get information with tag
for tag in soup.select('#fontScaleTarget > div.news_detail_view > div > div.boxing > h3'):
    title = tag.get_text()
for tag in soup.select('#fontScaleTarget > div.cont_aside > div.cont > div > div.news_detail_cont > div:nth-child(1) > div > div'):
    content = tag.get_text()
for tag in soup.select('#fontScaleTarget > div.cont_aside > div.cont > div > div.news_detail_cont > div:nth-child(2) > div > div.img > img'):
    imgUrl = tag['src']

# write information to csv file
wr.writerow([title, content, imgUrl])

# end of crawling

# close csv file
f.close()
