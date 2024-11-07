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
    url = f"https://api.github.com/users/{input_git_username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        repos = response.json()  # data returned is a
        # list of ‘repository’ entities

    # get user info
    url = f"https://api.github.com/users/{input_git_username}"
    user_response = requests.get(url)
    if user_response.status_code == 200:
        user_info = user_response.json()

    # get user profile picture
    login = user_info["login"]
    avatar = user_info["avatar_url"]
    git_birthday = user_info["created_at"]
    followers = user_info["followers"]
    following = user_info["following"]

    # get commit info
    results = []  # initialise list to contain dictionary for each repo
    for repo in repos:
        full_name = repo["full_name"]
        created_at = repo["created_at"]
        repo_response = requests.get(
            f"https://api.github.com/repos/{full_name}/commits"
        )
        if repo_response.status_code == 200:
            commits = repo_response.json()
        # get commit json for a repo
        last_commit = commits[0]
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
    user_info = {
        "avatar": avatar,
        "git_birthday": git_birthday,
        "followers": followers,
        "following": following,
        "login": login,
    }

    return render_template("repos.html", repos=results, user_info=user_info)


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
