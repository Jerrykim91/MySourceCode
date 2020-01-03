# import 
from flask import Flask, redirect, url_for
# instance creating
app = Flask(__name__)

# Defining the home page of our web
@ app.route("/") # page path setting 
def Home(): 
    # basic inline html
    return  "Hello this is our web site main page! plz enjoy <h1> HELLO </h1>"

# 동적 url
@app.route("/<name>")
def user(name):
    return f"Hello {name}!"
    
# 리디렉션 다른 페이지로 
@app.route("/admin") # /admin을 방문 할때 마다 home으로 리디렉션 
def admin():
    # url_for 기능을 사용하면 리디렉션하려는 함수의 이름을 출력 
	return redirect(url_for("Home"))

if __name__ == "__main__":
    app.run(debug = True)

# It works(ok) 