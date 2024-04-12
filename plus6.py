#!/usr/bin/env python
# coding: utf-8

# In[10]:


import os
import sys
import urllib.request
import urllib.parse
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import pandas as pd

client_id = "zCef739dSJ7Vgc0A6jXb"
client_secret = "HDOxDMIZ2m"
search_keyword = "진악산"
mountain_road = urllib.parse.quote(search_keyword)
display = 100

# 버전에 상관 없이 os에 설치된 크롬 브라우저 사용
driver = webdriver.Chrome()
driver.implicitly_wait(3)

contents = []

for start in range(1, 902, 100):
    url = f'https://openapi.naver.com/v1/search/blog?query={mountain_road}&display={display}&start={start}'
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
        json_data = response_body.decode('utf-8')
        data_dict = json.loads(json_data)

        # "items" 키에 해당하는 값에서 "link" 키에 해당하는 값만 추출하여 리스트에 저장
        links = [item['link'] for item in data_dict['items']]
        print(start)

        # 각 블로그의 텍스트 가져오기
        for i in links:
            try:
                print(i)
                driver.get(i)
                time.sleep(2)  # 대기시간 변경 가능

                iframe = driver.find_element(By.ID , "mainFrame") # id가 mainFrame이라는 요소를 찾아내고 -> iframe임
                driver.switch_to.frame(iframe) # 이 iframe이 내가 찾고자하는 html을 포함하고 있는 내용

                source = driver.page_source
                html = BeautifulSoup(source, "html.parser")
                
                # 기사 텍스트만 가져오기
                content = html.select("div.se-main-container")
                #  list합치기
                content = ''.join(str(content))

                # html태그제거 및 텍스트 다듬기
                pattern1 = '<[^>]*>'
                content = re.sub(pattern=pattern1, repl='', string=content)
                pattern2 = """[\n\n\n\n\n// flash 오류를 우회하기 위한 함수 추가\nfunction _flash_removeCallback() {}"""
                content = content.replace(pattern2, '')
                content = content.replace('\n', '')
                content = content.replace('\u200b', '')
                contents.append(content)
            except:
                continue
    else:
        print("Error Code:", rescode)

news_df = pd.DataFrame({'content': contents})
news_df.to_csv(f'{search_keyword}.csv', index=False, encoding='utf-8-sig')

# 크롬 드라이버 종료
driver.quit()


# In[11]:


import os
import sys
import urllib.request
import urllib.parse
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import pandas as pd

client_id = "zCef739dSJ7Vgc0A6jXb"
client_secret = "HDOxDMIZ2m"
search_keyword = "천주산"
mountain_road = urllib.parse.quote(search_keyword)
display = 100

# 버전에 상관 없이 os에 설치된 크롬 브라우저 사용
driver = webdriver.Chrome()
driver.implicitly_wait(3)

contents = []

for start in range(1, 902, 100):
    url = f'https://openapi.naver.com/v1/search/blog?query={mountain_road}&display={display}&start={start}'
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
        json_data = response_body.decode('utf-8')
        data_dict = json.loads(json_data)

        # "items" 키에 해당하는 값에서 "link" 키에 해당하는 값만 추출하여 리스트에 저장
        links = [item['link'] for item in data_dict['items']]
        print(start)

        # 각 블로그의 텍스트 가져오기
        for i in links:
            try:
                print(i)
                driver.get(i)
                time.sleep(2)  # 대기시간 변경 가능

                iframe = driver.find_element(By.ID , "mainFrame") # id가 mainFrame이라는 요소를 찾아내고 -> iframe임
                driver.switch_to.frame(iframe) # 이 iframe이 내가 찾고자하는 html을 포함하고 있는 내용

                source = driver.page_source
                html = BeautifulSoup(source, "html.parser")
                
                # 기사 텍스트만 가져오기
                content = html.select("div.se-main-container")
                #  list합치기
                content = ''.join(str(content))

                # html태그제거 및 텍스트 다듬기
                pattern1 = '<[^>]*>'
                content = re.sub(pattern=pattern1, repl='', string=content)
                pattern2 = """[\n\n\n\n\n// flash 오류를 우회하기 위한 함수 추가\nfunction _flash_removeCallback() {}"""
                content = content.replace(pattern2, '')
                content = content.replace('\n', '')
                content = content.replace('\u200b', '')
                contents.append(content)
            except:
                continue
    else:
        print("Error Code:", rescode)

news_df = pd.DataFrame({'content': contents})
news_df.to_csv(f'{search_keyword}.csv', index=False, encoding='utf-8-sig')

# 크롬 드라이버 종료
driver.quit()




#




import os
import sys
import urllib.request
import urllib.parse
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import pandas as pd

client_id = "zCef739dSJ7Vgc0A6jXb"
client_secret = "HDOxDMIZ2m"
search_keyword = "천태산"
mountain_road = urllib.parse.quote(search_keyword)
display = 100

# 버전에 상관 없이 os에 설치된 크롬 브라우저 사용
driver = webdriver.Chrome()
driver.implicitly_wait(3)

contents = []

for start in range(1, 902, 100):
    url = f'https://openapi.naver.com/v1/search/blog?query={mountain_road}&display={display}&start={start}'
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
        json_data = response_body.decode('utf-8')
        data_dict = json.loads(json_data)

        # "items" 키에 해당하는 값에서 "link" 키에 해당하는 값만 추출하여 리스트에 저장
        links = [item['link'] for item in data_dict['items']]
        print(start)

        # 각 블로그의 텍스트 가져오기
        for i in links:
            try:
                print(i)
                driver.get(i)
                time.sleep(2)  # 대기시간 변경 가능

                iframe = driver.find_element(By.ID, "mainFrame")  # id가 mainFrame이라는 요소를 찾아내고 -> iframe임
                driver.switch_to.frame(iframe)  # 이 iframe이 내가 찾고자하는 html을 포함하고 있는 내용

                source = driver.page_source
                html = BeautifulSoup(source, "html.parser")

                # 기사 텍스트만 가져오기
                content = html.select("div.se-main-container")
                #  list합치기
                content = ''.join(str(content))

                # html태그제거 및 텍스트 다듬기
                pattern1 = '<[^>]*>'
                content = re.sub(pattern=pattern1, repl='', string=content)
                pattern2 = """[\n\n\n\n\n// flash 오류를 우회하기 위한 함수 추가\nfunction _flash_removeCallback() {}"""
                content = content.replace(pattern2, '')
                content = content.replace('\n', '')
                content = content.replace('\u200b', '')
                contents.append(content)
            except:
                continue
    else:
        print("Error Code:", rescode)

news_df = pd.DataFrame({'content': contents})
news_df.to_csv(f'{search_keyword}.csv', index=False, encoding='utf-8-sig')

# 크롬 드라이버 종료
driver.quit()



#


import os
import sys
import urllib.request
import urllib.parse
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import pandas as pd

client_id = "zCef739dSJ7Vgc0A6jXb"
client_secret = "HDOxDMIZ2m"
search_keyword = "첨찰산"
mountain_road = urllib.parse.quote(search_keyword)
display = 100

# 버전에 상관 없이 os에 설치된 크롬 브라우저 사용
driver = webdriver.Chrome()
driver.implicitly_wait(3)

contents = []

for start in range(1, 902, 100):
    url = f'https://openapi.naver.com/v1/search/blog?query={mountain_road}&display={display}&start={start}'
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
        json_data = response_body.decode('utf-8')
        data_dict = json.loads(json_data)

        # "items" 키에 해당하는 값에서 "link" 키에 해당하는 값만 추출하여 리스트에 저장
        links = [item['link'] for item in data_dict['items']]
        print(start)

        # 각 블로그의 텍스트 가져오기
        for i in links:
            try:
                print(i)
                driver.get(i)
                time.sleep(2)  # 대기시간 변경 가능

                iframe = driver.find_element(By.ID, "mainFrame")  # id가 mainFrame이라는 요소를 찾아내고 -> iframe임
                driver.switch_to.frame(iframe)  # 이 iframe이 내가 찾고자하는 html을 포함하고 있는 내용

                source = driver.page_source
                html = BeautifulSoup(source, "html.parser")

                # 기사 텍스트만 가져오기
                content = html.select("div.se-main-container")
                #  list합치기
                content = ''.join(str(content))

                # html태그제거 및 텍스트 다듬기
                pattern1 = '<[^>]*>'
                content = re.sub(pattern=pattern1, repl='', string=content)
                pattern2 = """[\n\n\n\n\n// flash 오류를 우회하기 위한 함수 추가\nfunction _flash_removeCallback() {}"""
                content = content.replace(pattern2, '')
                content = content.replace('\n', '')
                content = content.replace('\u200b', '')
                contents.append(content)
            except:
                continue
    else:
        print("Error Code:", rescode)

news_df = pd.DataFrame({'content': contents})
news_df.to_csv(f'{search_keyword}.csv', index=False, encoding='utf-8-sig')

# 크롬 드라이버 종료
driver.quit()



#


import os
import sys
import urllib.request
import urllib.parse
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import pandas as pd

client_id = "zCef739dSJ7Vgc0A6jXb"
client_secret = "HDOxDMIZ2m"
search_keyword = "초록봉"
mountain_road = urllib.parse.quote(search_keyword)
display = 100

# 버전에 상관 없이 os에 설치된 크롬 브라우저 사용
driver = webdriver.Chrome()
driver.implicitly_wait(3)

contents = []

for start in range(1, 902, 100):
    url = f'https://openapi.naver.com/v1/search/blog?query={mountain_road}&display={display}&start={start}'
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
        json_data = response_body.decode('utf-8')
        data_dict = json.loads(json_data)

        # "items" 키에 해당하는 값에서 "link" 키에 해당하는 값만 추출하여 리스트에 저장
        links = [item['link'] for item in data_dict['items']]
        print(start)

        # 각 블로그의 텍스트 가져오기
        for i in links:
            try:
                print(i)
                driver.get(i)
                time.sleep(2)  # 대기시간 변경 가능

                iframe = driver.find_element(By.ID, "mainFrame")  # id가 mainFrame이라는 요소를 찾아내고 -> iframe임
                driver.switch_to.frame(iframe)  # 이 iframe이 내가 찾고자하는 html을 포함하고 있는 내용

                source = driver.page_source
                html = BeautifulSoup(source, "html.parser")

                # 기사 텍스트만 가져오기
                content = html.select("div.se-main-container")
                #  list합치기
                content = ''.join(str(content))

                # html태그제거 및 텍스트 다듬기
                pattern1 = '<[^>]*>'
                content = re.sub(pattern=pattern1, repl='', string=content)
                pattern2 = """[\n\n\n\n\n// flash 오류를 우회하기 위한 함수 추가\nfunction _flash_removeCallback() {}"""
                content = content.replace(pattern2, '')
                content = content.replace('\n', '')
                content = content.replace('\u200b', '')
                contents.append(content)
            except:
                continue
    else:
        print("Error Code:", rescode)

news_df = pd.DataFrame({'content': contents})
news_df.to_csv(f'{search_keyword}.csv', index=False, encoding='utf-8-sig')

# 크롬 드라이버 종료
driver.quit()