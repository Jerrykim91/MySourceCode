# import 
# !pip install flask
from flask import Flask
# flask 설치 => !pip install flask

# 인스턴스 생성
app = Flask(__name__)

if __name__ == "__main__":
    app.run()
#  실행 됨 
