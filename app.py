from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    input_first_name = request.form.get("first-name")
    input_last_name = request.form.get("last-name")
    input_age = request.form.get("age")
    return render_template("hello.html", first_name=input_first_name, last_name=input_last_name, age=input_age)
