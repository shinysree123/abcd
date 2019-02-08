from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/home")
def ind():
    return render_template("page2.html")
@app.route("/about")
def ins():
    return "welcome to about page"
if(__name__=="__main__"):
    app.run(debug="true")