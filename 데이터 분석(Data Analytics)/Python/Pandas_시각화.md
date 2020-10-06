<br>

#### 3. 자주 사용하는 코드 - Pandas_시각화

<br><br>

# Pandas_시각화

주로 쓰는 모듈 `matplotlib`,``,``,

<br>

## 1. matplotlib

<br>

### 설정 
---
1) 임포트 

    ```py 
    import matplotlib.pyplot as plt # matplotlib
    %matplotlib inline              # 같이 선언 해줘야함 
    ```
<br>

2) 폰트 성정     
모듈을 부르면서 그 다음에 해야할일은 폰트를 설정해 줘야한다.    
    그래프를 그리다 보면 한글이 많이 깨지는것을 확인 할 수 있다.    
    그렇기 때문에 미연에 방지하고자 미리 코드를 선언하고 들어가도록 하겠다. 

    ```py
    # 폰트
    import platform

    if platform.system() == 'Darwin':    # 맥
        font_name = 'AppleGothic'
    elif platform.system() == 'Linux':   # 리눅스
        font_name = 'NanumGothic'
    elif platform.system() == 'Windows': # 윈도우
        font_name = 'Malgun Gothic'
    else:
        print('운영체제 적용불가 운영체제 확인 요망')

    plt.rc('font', family=font_name)
    ```
---

<br>

### 1) 파이차트 - Pie plot

<br>

```py
import matplotlib.pyplot as plt   # 맷폴렛- 그래프
%matplotlib inline


# ignore warnings
import warnings    # 워닝 방지
warnings.filterwarnings('ignore')

# 라벨
labels = ('A', 'B', 'C') #-> plt.legend(['A','B','C'])
data = [50, 30, 40] 

plt.figure(figsize=(6, 6))

# plt.pie로 생기는 요소를 다음처럼 리턴하여 값을 저장해두고 
patches, texts, autotexts = plt.pie(
    labels=labels,          # 각 이름
    labeldistance=1.1,      # 벌어짐
    x = data,               # 값
    explode=(0.1, 0.1, 0),  # pie가 튀어나오는지 정해줌  
    startangle=90,          # 각도
    shadow=False,           #그림자 
    counterclock=False,     # 시계방향으로 가는지, 시계 반대 방향으로 가는지 정해줌 
    autopct='%1.1f%%',      # pi 위에 표시될 글자 형태, 또한 알아서 %로 변환해서 알려줌 
    pctdistance=0.7,        # pct가 radius 기준으로 어디쯤에 위치할지 정함 
    colors=['grey', 'red', 'blue'],
)


## 도넛처럼 만들기
centre_circle = plt.Circle((0,0),0.50,color='white')
plt.gca().add_artist(centre_circle)

# ## label 색 변경 
# for t in texts:
#     t.set_color("green")
#     t.set_fontproperties(BMDOHYEON)
#     t.set_fontsize(50)

# ## pie 위의 텍스트를 다른 색으로 변경해주기 
# for t in autotexts:
#     t.set_color("white")
#     t.set_fontproperties(BMDOHYEON)
#     t.set_fontsize(20)

plt.tight_layout()
save_path = "../data"
plt.savefig(save_path)
plt.show()
```


<br><br>



## 2. 

<br>

```py

```

<br>



<br><br>


### 10) 그래프 이미지 저장 


<br>

```py
# 프린트 
fig = plt.figure(figsize=(20,12))
fig.savefig('클라우드.png')

```

<br><br>


## 2. s

<br>



```py

```

<br>


<br><br>


## 3. plotly

<br>

요즘에 가장 뜨고 있는 시각화 모듈이다. 

```py
# 설치 
# pip install plotly
import plotly
```

<br>


<br><br>



## 5. 공간분석 - 시각화 


### 1) 공간 분석 

<br>

```py
import plotly.express as px

fig = px.scatter_mapbox(df_caffee, lat="위도", lon="경도", hover_name="상호명", hover_data=["지번주소", "도로명주소"],
                        color_discrete_sequence=["#636EFA"], zoom=11, height=600)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

<br>

### 2) 공간 정보 오픈 플랫폼 

<br>

공간정보 오픈 프랫폼을 사용하기위해서는 필요함 -> [open api 발급](http://www.vworld.kr/dev/v4api.do)

```py
# VworldSatellite, VworldHybrid 타일 추가

fig = px.scatter_mapbox(df_caffee, lat="위도", lon="경도", hover_name="상호명", hover_data=["지번주소", "도로명주소"],
                        color_discrete_sequence=["#FFA15A"], zoom=11, height=600)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# 개인 api 코드 있음 
fig.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces', 
            "sourcetype": "raster",
            "source": [
                "http://api.vworld.kr/req/wmts/1.0.0/개인키입력/Satellite/{z}/{y}/{x}.jpeg"
            ]
        },
        {
            "sourcetype": "raster",
            "source": [
                "http://api.vworld.kr/req/wmts/1.0.0/개인키입력/Hybrid/{z}/{y}/{x}.png"
            ],
        }
      ])
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

<br>


### 3) 맵박스 밀도 열지도

<br>

```py
# 맵박스 밀도 열지도
import plotly.graph_objects as go

fig = go.Figure(go.Densitymapbox(lat=df_caffee['위도'], lon=df_caffee['경도'], radius=10))
fig.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "source": [
                "http://api.vworld.kr/req/wmts/1.0.0/개인키입력/Satellite/{z}/{y}/{x}.jpeg"
            ]
        },
        {
            "sourcetype": "raster",
            "source": [
                "http://api.vworld.kr/req/wmts/1.0.0/개인키입력/Hybrid/{z}/{y}/{x}.png"
            ],
        }
      ],
    mapbox_zoom=9,
    mapbox_center = {"lat": 35.14, "lon": 129.07}) 
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

<br><br>

## 6. 웹으로 그래프 보이기 

<br>

```py

import plotly.graph_objects as go # or plotly.express as px
fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)
# fig.add_trace( ... )
# fig.update_layout( ... )

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
```
<br><br>


<br>

---

<br>

## Reference <br>

- Plotly 참고자료_지구과학, GIS, 그리고 원격탐사 블로그 &nbsp; : &nbsp;<http://blog.daum.net/geoscience/1420> <br>
- Plotly 참고자료_하나씩 점을 찍어 나가며 &nbsp; : &nbsp;<https://dailyheumsi.tistory.com/118> <br>

<!-- <br>
<br>

## Practice makes perfect! <br> -->

<!-- - [내용](주소) -->