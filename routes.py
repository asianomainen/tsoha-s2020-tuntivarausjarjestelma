from flask import redirect, render_template, request, session, abort
from werkzeug.security import generate_password_hash
from app import app
import messages
import users
import lessons

@app.route("/")
def index():
    return render_template("/index.html")

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
            return render_template("/login.html")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["up"]
        hash_value = generate_password_hash(password)
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        phone = request.form["phone"]
        users.register(username, hash_value, first_name, last_name, email, phone)
        return redirect("/")

@app.route("/new_lesson", methods=["GET", "POST"])
def new_lesson():
    user_id = session["user_id"]
    if users.is_admin(user_id):
        if request.method == "GET":
            return render_template("new_lesson.html")
        if request.method == "POST":
            if session["csrf_token"] != request.form["csrf_token"]:
                abort(403)
            name = request.form["name"]
            spots = request.form["spots"]
            date = request.form["date"]
            starts = request.form["starts"]
            ends = request.form["ends"]

            lessons.new_lesson(name, spots, date, starts, ends)

            return redirect("/")
    else:
        abort(403)

@app.route("/sign_up", methods=["POST"])
def sign_up():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    user_id = session["user_id"]
    lesson_id = request.form["id"]

    lessons.sign_up(user_id, lesson_id)

    return redirect("/")

@app.route("/undo_sign_up", methods=["POST"])
def undo_sign_up():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    user_id = session["user_id"]
    lesson_id = request.form["lesson_id"]

    lessons.undo_sign_up(user_id, lesson_id)

    return redirect("/")

@app.route("/account/<int:id>")
def account(id):
    user_id = session["user_id"]
    if user_id == id or session["admin"] == True:
        user_information = users.account_information(id)
        return render_template("/account.html", id=id, user_information=user_information)

@app.route("/account_update/<int:id>", methods=["POST"])
def account_update(id):
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    phone = request.form["phone"]

    users.account_update(first_name, last_name, email, phone, id)

    return redirect(f"/account/{id}")

@app.route("/change_password/<int:id>", methods=["POST"])
def change_password(id):
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    phone = request.form["phone"]

    users.account_update(first_name, last_name, email, phone, id)

    return redirect(f"/account/{id}")

@app.route("/remove_account/<int:id>")
def remove_account(id):
    user_id = session["user_id"]
    if user_id == id or session["admin"] == True:
        lessons.remove_sign_ups(id)
        users.remove_account(id)
        if session["admin"] == True:
            return redirect("/all_users")
    else:
        abort(403)
    users.logout()
    return redirect("/")

@app.route("/all_users")
def all_users():
    user_id = session["user_id"]
    if users.is_admin(user_id):
        all_users = users.get_users()
        return render_template("/all_users.html", users=all_users)
    else:
        abort(403)

@app.route("/admin_all_lessons")
def all_lessons():
    user_id = session["user_id"]
    if users.is_admin(user_id):
        all_lessons = lessons.get_lessons()
        return render_template("/all_lessons.html", lessons=all_lessons)
    else:
        abort(403)

@app.route("/user_all_lessons")
def al_lessons():
    try:
        user_id = session["user_id"]
        all_lessons = lessons.get_lessons()
        user_lessons = lessons.get_user_lessons(user_id)
        return render_template("/lessons.html", lessons=all_lessons, user_lessons=user_lessons)
    except:
        all_lessons = lessons.get_lessons()
        return render_template("/lessons.html", lessons=all_lessons)

@app.route("/lesson/<int:id>")
def lesson(id):
    user_id = session["user_id"]
    if users.is_admin(user_id):
        lesson = lessons.lesson_information(id)
        participants = lessons.get_participants(id)
        return render_template("/lesson.html", id=id, lesson_information=lesson, 
                                                      participants=participants)
    else:
        abort(403)

@app.route("/lesson_update/<int:id>", methods=["POST"])
def lesson_update(id):
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    name = request.form["name"]
    spots = request.form["spots"]
    date = request.form["date"]
    starts = request.form["starts"]
    ends = request.form["ends"]

    lessons.lesson_update(name, spots, date, starts, ends, id)

    return redirect("/all_lessons")

@app.route("/remove_lesson/<int:id>")
def remove_lesson(id):
    lessons.remove_lesson(id)
    return redirect("/all_lessons")

@app.route("/remove_participant/<int:user_id>/<int:lesson_id>")
def remove_participant(user_id, lesson_id):
    lessons.remove_participant(user_id, lesson_id)
    return redirect(f"/lesson/{lesson_id}")

@app.route("/my_lessons/<int:id>")
def my_lessons(id):
    user_id = session["user_id"]
    if user_id == id:
        all_user_lessons = lessons.get_user_lessons(user_id)
        return render_template("/my_lessons.html", lessons=all_user_lessons)
    else:
        abort(403)

@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "GET":
        return render_template("/feedback.html")
    if request.method == "POST":
        try:
            if session["csrf_token"] != request.form["csrf_token"]:
                abort(403)
            message = request.form["message"]
            user_id = session["user_id"]
            messages.feedback(user_id, message)
        except:
            message = request.form["message"]
            email = request.form["email"]
            messages.anonymous_feedback(email, message)

    return redirect("/")
