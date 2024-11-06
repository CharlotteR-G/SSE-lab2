from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/gitSubmit", methods=["POST"])
def gitSubmit():
    input_git_username = request.form.get("username")
    # get repos
    response = requests.get(f"https://api.github.com/users/{input_git_username}/repos")
    if response.status_code == 200:
        repos = response.json()  # data returned is a list of ‘repository’ entities
    # get commit info
    results = []  # initialise list to contain dictionary for each repo
    for repo in repos:
        full_name = repo["full_name"]
        created_at = repo["created_at"]
        repo_response = requests.get(
            f"https://api.github.com/users/{full_name}/commits"
        )  # get commit json for a repo
        last_commit = repo_response[0]
        commit_hash = last_commit["sha"]
        author = last_commit["commit"]["author"]["name"]
        date = last_commit["commit"]["author"]["date"]
        message = last_commit["commit"]["message"]
        results.append(
            {
                "full_name": full_name,
                "created_at": created_at,
                "hash": commit_hash,
                "author": author,
                "date": date,
                "message": message,
            }
        )

    return render_template("repos.html", repos=results)


"""
@app.route("/submitGit/commits", methods=["POST"])
def github():
    input_git_username = request.form.get("username")
    response = requests.get(f"https://api.github.com/users/{input_git_username}/repos")
    results = []
    if response.status_code == 200:
        repos = response.json() # data returned is a list of ‘repository’ entities
        for repo in repos:
            full_name = repo['full_name']
            repo_response = requests.get(f"https://api.github.com/users/{full_name}/commits")
            ## Something
            results.append({'full_name': full_name})
    return render_template("api_test_output.html", commits=results)
"""


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
    return process_query(q)


def process_query(q):
    if q == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    if q == "asteroids":
        return "Unknown"
