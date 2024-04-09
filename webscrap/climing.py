from bs4 import BeautifulSoup
import requests
import re
import time
import os
import sys
import urllib.request
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')
plt.rc('axes', unicode_minus=False)

df = pd.read_json('mountain_100.json', encoding='UTF-8')
df = pd.json_normalize(df['response']['body']['items']['item'])
df = df.rename(
  columns={'lot': '경도', 'frtrlId': '아이디', 'ctpvNm': '시도명', 'crtrDt': '데이터추출일시', 'aslAltide': '해발고도', 'mtnCd': '산코드',
           'addrNm': '주소', 'frtrlNm': '산명', 'lat': '위도'
           })

# 웹드라이버 설정
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# 버전에 상관 없이 os에 설치된 크롬 브라우저 사용
driver = webdriver.Chrome()
driver.implicitly_wait(3)
# 버전에 상관 없이 os에 설치된 크롬 브라우저 사용


# Naver API key 입력
client_id = "ShIovNz7SXGAFNygBoVx"
client_secret = "1Gh1DzPsn3"

# selenium으로 검색 페이지 불러오기 #
naver_urls = []
postdate = []
titles = []

# 검색을 끝낼 페이지 입력
menu = input('100대 명산 채크 [명산]/ 일반 검색 [Enter]')

if (menu == '명산'):
  # 검색어 입력
  keword = input("검색할 키워드를 입력해주세요:")
  encText = urllib.parse.quote(keword)
  farst = input("\n크롤링을 시작 위치를 입력해주세요. (기본값:1, 최대값:100):")
  if farst == "":
    farst = 1
  else:
    end = int(end)
  end = input("\n반복될 카운팅을 입력해주세요. (기본값:1, 최대값:100):")
  if end == "":
    end = 1
  else:
    end = int(end)
  print(farst, " ~", int(farst) + end, "페이지 까지 크롤링을 진행 합니다")
else:
  keword = input("검색할 키워드를 입력해주세요:")
  encText = urllib.parse.quote(keword)
  farst = input("\n크롤링을 시작 위치를 입력해주세요. (기본값:1, 최대값:100):")
  if farst == "":
    farst = 1
  else:
    end = int(end)
  end = input("\n시작부터 마지막 위치 입력해주세요. (기본값:1, 최대값:100):")
  if end == "":
    end = 1
  else:
    end = int(end)
  print(farst, " ~", int(farst) + end, "페이지 까지 크롤링을 진행 합니다")

# 한번에 가져올 페이지 입력
display = input("\n한번에 가져올 페이지 개수를 입력해주세요.(기본값:10, 최대값: 100):")
if display == "":
  display = 10
else:
  display = int(display)
print("\n한번에 가져올 페이지 : ", display, "페이지")
namedata = keword

for start in range(end):
  print(start + 1 + int(farst))
  url = "https://openapi.naver.com/v1/search/blog?query=" + encText + "&start=" + str(
    start + 1 + int(farst)) + "&display=" + str(display + 1)  # JSON 결과
  request = urllib.request.Request(url)
  request.add_header("X-Naver-Client-Id", client_id)
  request.add_header("X-Naver-Client-Secret", client_secret)
  response = urllib.request.urlopen(request)
  rescode = response.getcode()
  if (rescode == 200):
    response_body = response.read()

    data = json.loads(response_body.decode('utf-8'))['items']
    for row in data:
      if ('blog.naver' in row['link']):
        naver_urls.append(row['link'])
        postdate.append(row['postdate'])
        title = row['title']
        # html태그제거
        pattern1 = '<[^>]*>'
        title = re.sub(pattern=pattern1, repl='', string=title)
        titles.append(title)
    time.sleep(2)
  else:
    print("Error Code:" + rescode)
  farst = int(farst)
  display = int(display)
  farst += display
  farst -= 1

###naver 기사 본문 및 제목 가져오기###

# ConnectionError방지
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/98.0.4758.102"}

contents = []
comments_texts = []
try:
  for i in naver_urls:
    print(i)
    driver.get(i)
    time.sleep(5)  # 대기시간 변경 가능

    iframe = driver.find_element(By.ID, "mainFrame")  # id가 mainFrame이라는 요소를 찾아내고 -> iframe임
    driver.switch_to.frame(iframe)  # 이 iframe이 내가 찾고자하는 html을 포함하고 있는 내용

    source = driver.page_source
    html = BeautifulSoup(source, "html.parser")
    # 검색결과 확인용
    # with open("Output.txt", "w") as text_file:
    #     text_file.write(str(html))

    # 기사 텍스트만 가져오기
    content = html.select("div.se-main-container")
    #  list합치기
    content = ''.join(str(content))

    # html태그제거 및 텍스트 다듬기
    content = re.sub(pattern=pattern1, repl='', string=content)
    pattern2 = """[\n\n\n\n\n// flash 오류를 우회하기 위한 함수 추가\nfunction _flash_removeCallback() {}"""
    content = content.replace(pattern2, '')
    content = content.replace('\n', '')
    content = content.replace('\u200b', '')
    contents.append(content)

  name = namedata + 'blog.csv'
  print(name)
  news_df = pd.DataFrame({'title': titles, 'content': contents, 'date': postdate})
  news_df.to_csv('blog.csv', index=False, encoding='utf-8-sig')
  os.rename('blog.csv', name)
except:
  contents.append('error')
  news_df = pd.DataFrame({'title': titles, 'content': contents, 'date': postdate})
  news_df.to_csv('blog.csv', index=False, encoding='utf-8-sig')