from bs4 import BeautifulSoup
from urllib.request import urlopen

host = 'https://www.naver.com'
html = urlopen(host)
bsObj = BeautifulSoup(html.read(), 'html.parser')
print(bsObj)
import re

# ^: 첫 시작하는 문구 확인
# ?: 앞문자가 0또는1개
# [a-z,.]: 소문자와 .을 허용
# *: 0개 이상
a = bsObj.findAll('a')
# print(a)