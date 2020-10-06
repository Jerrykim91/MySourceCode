<br>

#### 1. 자주 사용하는 코드  - 크롤링, Crawling

<br><br>

# 크롤링

<br>

## 1. 특수 문자 제거 - 정규식 <br>

<br>

텍스트에 포함되어 있는 특수 문자 제거


```py
import re  # 정규식 모듈 불러오기 

def cleanText(data):
    """
    텍스트에 포함되어 있는 특수 문자 제거
    # import re
    """
    txt = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', data)
    # txt = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', raw)
    return txt
```

<br><br>


## 2. 필요한 요소 가지고 오기

find(복수는 find_all)와 select(한 개 찾을때에는 select_one) 를 이용한 방법
select 하나만 써도 문제 없이 크롤링 가능
<br>

```py
soup.select('원하는 정보')  # select('원하는 정보') -->  단 하나만 있더라도, 복수 가능한 형태로 되어있음

soup.select('태그명')
soup.select('.클래스명')
soup.select('상위태그명 > 하위태그명 > 하위태그명')
soup.select('상위태그명.클래스명 > 하위태그명.클래스명')    # 바로 아래의(자식) 태그를 선택시에는 > 기호를 사용
soup.select('상위태그명.클래스명 하~위태그명')              # 아래의(자손) 태그를 선택시에는   띄어쓰기 사용
soup.select('상위태그명 > 바로아래태그명 하~위태그명')     
soup.select('.클래스명')
soup.select('#아이디명')                  # 태그는 여러개에 사용 가능하나 아이디는 한번만 사용 가능함! ==> 선택하기 좋음
soup.select('태그명.클래스명')
soup.select('#아이디명 > 태그명.클래스명')
soup.select('태그명[속성1=값1]')
```

<br><br>



<!-- ## 3.

<br>

```py

```

<br> -->


<!-- 
## 3.

<br>

[참조](https://somjang.tistory.com/entry/Python%EC%9D%B8%EC%8A%A4%ED%83%80%EA%B7%B8%EB%9E%A8-%EC%86%8D-%ED%9D%91%EB%8B%B9%EB%B2%84%EB%B8%94%ED%8B%B0-%EB%B6%84%EC%84%9D%ED%95%B4%EB%B3%B4%EA%B8%B0)

[참조](https://dejavuqa.tistory.com/110)

```py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.coreSpriteRightPaginationArrow')))

``` -->

<br>


<!-- 
## 4. 인스타 크롤링 

<br>

```py

from selenium import webdriver
import time
import re
from bs4 import BeautifulSoup
import csv
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def select_first(driver):
    """
    게시물 이미지 클릭
    """
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div._9AhH0')))
    first = driver.find_element_by_css_selector("div._9AhH0")
    first.click()
    
def get_content(driver):
    """
    html 정보 수집후 
    내용,해시태그,작성일자,좋아요 수, 위치정보  가지고 오기 
    # 정규식 활용 
    # 리스트 형식으로 저장 
    """
    # ① 현재 페이지 html 정보 가져오기
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    # ② 본문 내용 가져오기
    try:
        content = soup.select('div.C4VMK > span')[0].text 
    except:
        content = ' '
    # ③ 본문 내용에서 해시태그 가져오기(정규식 활용)
    try:
        tags = re.findall(r'#[^\s#,\\]+', content)  
    except:
        tags = ' '
    # ④ 작성일자 정보 가져오기
    date = soup.select('time._1o9PC.Nzb55')[0]['datetime'][:10]
    # ⑤ 좋아요 수 가져오기
    try:
        like = soup.select('div.Nm9Fw > button')[0].text[4:-1]   
    except:
        like = 0
    # ⑥ 위치정보 가져오기
    try: 
        place = soup.select('div.M30cS')[0].text
    except:
        place = ' '
    
    content = re.findall(r'[\s\w]+', content)
    # ⑦ 수집한 정보 저장하기
    data = [content, date, like, place, tags]
    return data

def move_next(driver):
    
    """
    다음페이지 클릭 옵션 
    """
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.coreSpriteRightPaginationArrow')))
    right = driver.find_element_by_css_selector ('a.coreSpriteRightPaginationArrow')
    right.click()

start = time.time() # 시작시간 
driver = webdriver.Chrome("C:/C19/driver/chromedriver.exe") # 드라이버 위치 

# 인스타그램 접속하기 ####################
driver.get('https://www.instagram.com/?hl=ko')

time.sleep(2)
#########################################



# 계정 정보 입력 ########################

email = 'barbie329@naver.com'   ### 계정 정보 수정 필요
input_id = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[0]
input_id.clear()
input_id.send_keys(email)

password = 'Dudwo*960329' ### 비번 정보 수정 필요
input_pw = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[1]
input_pw.clear()
input_pw.send_keys(password)
input_pw.submit()

time.sleep(2)
#########################################


# 검색어 작성 ###########################

driver.get("https://www.instagram.com/explore/tags/" + "캠핑") # '캠핑'이라는 검색어 입력

time.sleep(2)
#########################################

select_first(driver) # 게시물 이미지 클릭
cnt=0

# 검색어 결과 몇개 나올지 몰라서 무조건 실행
running=True
while running:
    get = True
    point = 0
    # 게시물 못 들고 올 경우를 고려해서 들고올 수 있을때 까지 실행
    while get:
        Step = time.time() # 시작시간 
        try:
            data = get_content(driver)
            # 2020년 아니면 pass 
#             if data[1][:4] != '2020':
#                 continue
            # 여기서 부터 1~6 해당되면 동작    
            if data[1][6] < '7' and data[1][:4] == '2020':
#                 print(data[1][6])
                tags= ' '.join(data[4])
                txt = ' '.join(data[0])
                dic={'content':[txt],'date':[data[1]],'like':[data[2]],'like':[data[2]], 'tags': [tags] ,'palce':[data[3]]}
                print(dic)
                dic = pd.DataFrame(dic)
            else:
                get = False

        except:
            time.sleep(3)
            
    Step_time=(time.time() - Step)/60
    print(f"동작 체크 : {data[1]})
    
    cnt+=1
    if cnt%100==0:
        Step_time=(time.time() - Step)/60
        dic.to_csv('C:/C19/data/InstagramCraw/instagram.csv',mode ='a',header=False,encoding = 'utf-16', index=False)
        print("저장완료 ! 100단위 시간: %.2f[min] "%float(Step_time))
        print(cnt)
    try:# 다음으로 누르는 버튼이 없다면 except로 가서 running = Fasle가 되어서 제일 위에있는 while문 탈출
        move_next(driver)  # 다음 페이지로 이동 
#         running = False
    except:
        running = False
        
all_time=(time.time() - start)/60            
print("총 시간: %.2f[min]"%float(all_time))

```

<br> -->





<br>

---

<br>

## Reference <br>

<!-- - 파이썬 코딩도장 &nbsp; : &nbsp;<https://dojang.io/> <br> -->
<!-- 
<br>
<br>

## Practice makes perfect! <br>

- [내용](주소) -->