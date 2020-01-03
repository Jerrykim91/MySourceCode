from flask import Flask

app = Flask(__name__)

# Defining the home page of our web
#  라우터 생성
@ app.route("/") # page path setting 페이지 경로 설정 

def Home(): 
    # basic inline html
    return  "Hello this is our web site main page! plz enjoy <h1> HELLO </h1>"

if __name__ == "__main__":
    app.run()

# 동작  ok 