# 템플릿(template) 사용법
# from flask import Flask, redirect, url_for

#Step 1 :Import the render_template function from flask
from flask import Flask, render_template

# instance creating
app = Flask(__name__)

# Defining the home page of our web
@ app.route("/") # page path setting 
def home(): 
    # basic inline html
    #return  "Hello this is our web site main page! plz enjoy <h1> HELLO </h1>"
    return render_template("index.html")

# 동적 url
@app.route("/<name>")
def user(name):
    return f"Hello {name}!"
    
# 리디렉션 다른 페이지로 
@app.route("/admin") # /admin을 방문 할때 마다 home으로 리디렉션 
def admin():
    # url_for 기능을 사용하면 리디렉션하려는 함수의 이름을 출력 
	return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug = True)

# It works(ok) 