### Step 0. 준비
import sys    # 시스템
import os     # 시스템

import pandas as pd    # 판다스 : 데이터분석 라이브러리
import numpy as np     # 넘파이 : 숫자, 행렬 데이터 라이브러리

from bs4 import BeautifulSoup                 # html 데이터 전처리
from selenium import webdriver                # 웹 브라우저 자동화
from selenium.webdriver.common.by import By   #element 선택 함수 
import time                                   # 시간 지연
from tqdm import tqdm_notebook                # 진행상황 표시

url = "https://blog.naver.com/ukbluebird"
driver = webdriver.Chrome("/Users/jeongjinchan/Downloads/chromedriver_mac64/chromedriver.exec")

url_load = open("test.txt","r")
storeXlsx = open("ttt.txt","w")
# 수집한 url 돌면서 데이터 수집
for url in url_load:
    # 글 띄우기
    print(url)
    driver.get(url)   # 글 띄우기
    time.sleep(1)
    #crawling
    try :
        driver.switch_to.frame("mainFrame")
        time.sleep(1)
        #전체보기 클릭
        #driver.find_element(By.XPATH,'//*[@id="category0"]').click()
        #time.sleep(1)

        count = 0
        #제목 크롤링                     
        #내용 크롤링
        contents = driver.find_elements(By.CLASS_NAME,'se-component-content')
        content_list = []
        for content in contents:
            if(count==0) : 
                title = content.text #title
            count+=1
        content_str = ' '.join(content_list)
        print(title)
        storeXlsx.write(title)
    except :
        print("실패" + url)
        driver.close()
        time.sleep(1)
        continue


