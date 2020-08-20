import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com/'
ttl_lst = []

soup = BeautifulSoup(requests.get(url).text,features="lxml")
title = soup.findAll('title')
for row in title:
     ttl_lst.append(row.text)

print(ttl_lst)
