# 크롤링_ 날씨 
#---

#  크롤링 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# datetime 
from datetime import datetime
from datetime import timedelta

#  분석용 툴 
import pandas as pd
import numpy as np
import time


# 드라이버옵션설정 
options = webdriver.ChromeOptions()

# options.add_argument('headless') 
options.add_argument("window-size=1920x1080")
# user-agent 
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  

start = time.time()

# 드라이버 가지고 오기 
path = './data/chromedriver.exe' 
driver = webdriver.Chrome(path,options=options)

# 드라이버에 진입할 경로 전달
driver.get("https://www.weather.go.kr/w/weather/now.do")
time.sleep(1)