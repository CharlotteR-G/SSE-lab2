from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_first_name = request.form.get("first-name")
    input_last_name = request.form.get("last-name")
    input_student_number = request.form.get("student-number")
    input_age = request.form.get("age")
    input_degree = request.form.get("degree-level")
    input_module = request.form.get("module")
    return render_template(
        "submission.html",
        first_name=input_first_name,
        last_name=input_last_name,
        age=input_age,
        student_number=input_student_number,
        degree_level=input_degree,
        module=input_module,
    )

@app.route("/query")
def get_query():
    q = request.args.get("q")


def process_query(q):
    if q == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    if q == "astroids":
        return "Unknown"