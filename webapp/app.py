from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
    return "welcome to my website"
@app.route("/home")
def ind():
    return "welcome"
@app.route("/about")
def ins():
    return "welcome to home page"
if(__name__=="__main__"):
    app.run(debug="true")