<br>

#### 2. 자주 사용하는 코드  - 판다스, Pandas

<br><br>

# 판다스, Pandas

주로 쓰는 인코딩 `euc-kr, utf-8, CP949, utf-8-sig`

<br>

## 1. 데이터 로드 방법 

<br>

### 1) 포맷팅 형식

```py
path = './data/%s.csv' 
df = pd.read_csv(path %'파일이름')
```

<br>

### 2) os 와 glob을 이용하여 path를 가져와 데이터로드하는 방식

<br>

```py
import os
import glob

## 1번 방법 
# 변수에 경로할당
path = 'C:/data/'
df = pd.read_csv(glob.glob(path+'*')[0])

## 2번 방법 
# 현재 내 경로 
os.getcwd()
# ['C:\\stock']

# 데이터 경로 
dirpaths = glob.glob(os.getcwd()+"/data"+"/*")
# ['C:\\stock/data\\상장법인목록.xls']
df = pd.read_csv(dirpaths[0]) 

# 경로 내에 데이터 리스트 확인 
os.listdir(os.getcwd()+"/data")
# ['상장법인목록.xls']
```
<br>

위 코드는 데이터 개수가 변경되면 수정 해야해야한다는 번거로움이 있다. 

개인적으로 이 방식이 좋은 방식이 아닌 것은 알지만 오타방지용으로 많이 사용한다. 

<!-- ### 3)  -->


<br><br>


## 2. 데이터 확인 

<br>

### 1) 기본 정보확인 

```py
# info 
df.info()

# shape   ->  데이터 길이 (인덱스, 컬럼)
df.shape

# columns ->  컬럼종류
df.columns
```

<br>


### 2) 특정 위치 정보 확인 

원하는 위치의 컬럼과 인덱스 길이를 확인한다. 

```py 
idxNum = 10        # 인덱스 길이
colsLen = [0,2,-1] # 컬럼 위치값 

# 원하는 위치의 컬럼과 인덱스 길이를 확인 
df.iloc[:idxNum, colsLen]
```

<br><br>


## 3. 결측값 확인하는 코드 

<br>

### 1) 널값 확인 

```py
# 데이터 프레임의 전체 널값 확인 
df.isnull().sum()

# 결측치인 아이만 출력 
df[df.'컬럼이름'.isnull()==True]

```

<br>

### 2) 널값 확인 및 제거 

```py
cols_info = {
            'patient_id': '환자 ID',
            'sex': '성별',
            'age': '나이',
            'country': '국적'}

# 결측확인 
for col in df.columns:
    print(f'{cols_info[col]} = ', df[col].isnull().sum())

# 결측 비율화
for col in df.columns:
    percent = df[col].isnull().sum() / df[col].shape[0]
    msg = 'column: {:>20}\t Percent of NaN value: {:.2f}%'.format(col, 100 * (percent))
    print(msg)
```

<br><br>

## 4. `dict()` 정렬(딕트정렬)

<br>

`list()` 안의 중복값의 개수를 확인하고 중복수에 따라 순위를 확인하자 한다. 

그래서 `dict()`를 이용하여 작업을 진행 
- 리스트안의 중복된 값의 개수


```py
data = dict()
for cnt in allData:
    try: data[cnt] += 1
    except: data[cnt]=1
```

<br>

data는 중복값과 그 중복값의 개수를 보여준다.     

이렇게 만들어진 data를 `sorted(data)` 이용해 정렬한다.      

확인해 보니 defult 값 오름차순이며 keys 기준이라 옵션을 이용해 vaules 기준으로 그리고 내림차순으로 변경한다.      

여기서 오름차순을 내림차순으로 변경하는것은 
`sorted(data,reverse=True)` 를 이용하면 되지만 

keys 기준을 vaules 기준으로 바꾸는것 같이 특정 기준을 변경하는것은 따로 패키지를 이용하여 진행해야한다. 다행히도 번거롭게 설치 할 필요는 없다.

`import operator` 를 이용하여 진행하면 된다.

operator의 자세한 내용은 [참고](https://docs.python.org/ko/3.7/library/operator.html) 확인해보면된다.   

여기서 `itemgetter()` 안에 들어가는 수는 `0` 은 키 기준 , `1` 값 기준이다. 

임포트를 한 후 이렇게 함수 내부에 파라미터 값을 `key=operator.itemgetter(1)` 으로 지정하면 vaules 기준으로 내림차순의 데이터를 확인 가능하다.         

```py
sorted(data.items(),reverse=True, key=operator.itemgetter(1))
``` 
타이을 확인해보면 `list`로 형식으로 담기게 되는데 인덱싱을 이용하여 원하는 형태로 추출이 가능하다.      

<br><br>
 
## 5.  데이터 프레임 생성 

<br>

### 1 ) 보유 데이터 기반으로 데이터 프레임 생성 

`list`, `dict` 에 담긴 데이터를 기반으로 데이터 프레임 생성 

```py
data = dict() or list()

df = pd.DataFrame(data) # 프레임 생성 

print(df)
```

<br>


### 2 ) 생성, 활용해서 데이터 프레임 생성      

<br>

데이터를 생성 혹은 활용해서 데이터 프레임 생성      

리스트내포를 이용해서 

```py
df_data = pd.DataFrame( columns = ("fst","sed","trd") )

df_data_1 = df_data
for i in range(5):
    df_data_1.loc[i] = [(i+1)*(n+1) for n in range(3)]

print(df_data_1)
```

<br>

### 3 ) 데이터 프레임 생성 후 특정 컬럼 추가 

<br>

특정 컬럼에 데이터 추가

```py
df_data = pd.DataFrame( columns = ("fst","sed","trd") )

# 특정 컬럼에 데이터 추가 
df_data_2 = df_data
df_data_2.trd = [date]

print(df_data_2)
```

<br><br>

## 6. 데이터 병합 

<br>

판다스와 for 문을 이용해 데이터 병합

```py
pathName = 'C:\data\%s' 

dataList = list()
cnt = 0
# glob 경로를 추출 -> 경로를 read_csv
for pth in glob.glob(pathName%'Camp'+'/*'):
    # read_csv를 이용해 파일을 읽어서 변수에 담는다 
    origin  = pd.read_csv( pth, index_col=False)
    cnt = cnt + len(origin) # 데이터 검증을 위한 누적코드
    
    print(cnt)
    dataList.append(origin)

# 리스트에 담긴 데이터프레임을 concat을 이용해 병합한후 csv로 저장 
CatList= pd.concat(dataList,axis=0, ignore_index=True)
# axis=0은 수직, axis=1은 수평으로 병합
# ignore_index=True는 순서를 무시하고 순서대로 정렬
CatList.to_csv('C:/data/%s.csv'% f'Camp', index=False, mode='w', encoding='utf-8')
```

<br><br>


## 7. 여러개 문자를 기준으로 문자열 자르기 

<br>

### 1) `re.findall()`을 이용하는 방법 

- `re.findall(pattern, string, flags=0)`을 쓰는 방법

```py
import re
DATA = "Hey, you - what are you doing here!?"
print re.findall(r"[\w']+", DATA)
# Prints ['Hey', 'you', 'what', 'are', 'you', 'doing', 'here']
```
<br>

### 2) `re.split()`을 이용하는 방법 

- `re.split(pattern, string[, maxsplit=0])`을 쓰는 방법

```py
import re
DATA = "Hey, you - what are you doing here!?"
print re.split('\W+', DATA) # ['Hey', 'you', 'what', 'are', 'you', 'doing', 'here', '']
```

<br>

### 3)` replace()`한 후 `split()`하는 방법

- `replace()`와 `split()`를 사용하여 문자열을 자를 수 있다. 

```py
'a;bcd,ef g'.replace(';',' ').replace(',',' ').split() = ['a', 'bcd', 'ef', 'g']
```

<br><br>


## 8. 엑셀 데이터 시트 여러개 일때 출력 

<br>

말 그대로 엑셀파일은 하나지만 시트가 여러장일 경우 이 방법을 사용해서 데이터를 로 할 수 있다.  

```py
# 데이터 시트 여러개 일때 출력 
sheet_Name = [
    '2015 부산 강수량', '2016 부산 강수량',
    '2017 부산 강수량', '2018 부산 강수량',
    '2019 부산 강수량', '2020 부산 강수량' ]

def read_exel(xlse_path, sheet_Name) :
    exel_file = pd.ExcelFile(xlse_path)
    data = exel_file.parse(sheet_Name)
    return data

# data = read_exel(data_path, sheet_Name[])
```

<br><br>


## 9. 피클 

<br>

### 1) 피클 - 새로만들기  

```py 
import pickle # 모듈불러오기 

# save data
with open( '파일이름'+'.pickle','wb') as fw:
    pickle.dump(stockInfo, fw)
    
```

<br>

```py

```

<br>





<br>

---

<br>

## Reference <br>

- HashCode &nbsp; : &nbsp;<https://hashcode.co.kr/questions/493/%EC%97%AC%EB%9F%AC%EA%B0%9C-%EB%AC%B8%EC%9E%90%EB%A5%BC-%EA%B8%B0%EC%A4%80%EC%9C%BC%EB%A1%9C-%EB%AC%B8%EC%9E%90%EC%97%B4%EC%9D%84-%EC%9E%90%EB%A5%B4%EB%8A%94-%EB%B0%A9%EB%B2%95%EC%9D%B4-%EC%9E%88%EB%82%98%EC%9A%94> <br>

<!-- <br>
<br>

## Practice makes perfect! <br> -->

<!-- - [내용](주소) -->