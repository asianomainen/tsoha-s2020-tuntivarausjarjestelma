from app import app
import users
import lessons
from flask import redirect, render_template, request, session
from werkzeug.security import generate_password_hash


@app.route("/")
def index():
    all_lessons = lessons.get_lessons()
    return render_template("/index.html", lessons=all_lessons)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("/login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("/index.html")

@app.route("/logout")
def logout():
        users.logout()    
        return redirect("/")

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hash_value = generate_password_hash(password)
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        phone = request.form["phone"]
        if users.register(username, hash_value, first_name, last_name, email, phone):
            return redirect("/")
        else:
            return redirect("/")

@app.route("/new_lesson", methods=["GET", "POST"])
def new_lesson():
    if request.method == "GET":
        return render_template("new_lesson.html")
    if request.method == "POST":
        name = request.form["name"]
        spots = request.form["spots"]
        date = request.form["date"]
        start = request.form["start"]
        duration = request.form["duration"]

        lessons.new_lesson(name, spots, date, start, duration)

        return redirect("/")

@app.route("/sign_up", methods=["POST"])
def sign_up():
    username = session["username"]
    lesson_id = request.form["id"]

    lessons.sign_up(username, lesson_id)

    return redirect("/")

@app.route("/undo_sign_up", methods=["POST"])
def undo_sign_up():
    username = session["username"]
    lesson_id = request.form["id"]

    lessons.undo_sign_up(username, lesson_id)

    return redirect("/")

@app.route("/account")
def account():
    username = session["username"]
    user_information = users.account_information(username)

    return render_template("/account.html", user_information=user_information)

@app.route("/account_update", methods=["POST"])
def account_update():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    phone = request.form["phone"]
    username = session["username"]

    users.account_update(first_name, last_name, email, phone, username)

    return redirect("/account")

@app.route("/remove_account")
def remove_account():
    username = session["username"]

    users.remove_account(username)

    return redirect("/")
