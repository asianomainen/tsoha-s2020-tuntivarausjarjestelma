from flask import Flask
from flask import redirect, render_template, request, session, flash
from flask.signals import Namespace
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from os import getenv, name, stat_result

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
app.secret_key = getenv("SECRET_KEY")

@app.route("/")
def index():
    sql = "SELECT id, name, spots, date, start, duration FROM lessons"
    result = db.session.execute(sql)
    lessons = result.fetchall()
    return render_template("index.html", lessons=lessons)

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    sql = "SELECT password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if user == None:
        flash("Käyttäjätunnus tai salasana väärin.")
        return render_template("index.html")
    else:
        hash_value = user[0]
        if check_password_hash(hash_value,password):
            session["username"] = username
            return redirect("/")
        else:
            flash("Käyttäjätunnus tai salasana väärin.")
            return render_template("index.html")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")
    
@app.route("/new_user",methods=["POST"])
def new_user():
    return render_template("/new_user.html")
    
@app.route("/new_user_login",methods=["POST"])
def new_user_login():
    username = request.form["username"]
    password = request.form["password"]
    hash_value = generate_password_hash(password)
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    phone = request.form["phone"]

    sql = "INSERT INTO users (username, password, first_name, last_name, email, phone) VALUES (:username, :password, :first_name, :last_name, :email, :phone)"
    db.session.execute(sql, {"username":username, "password":hash_value, "first_name":first_name, "last_name":last_name, "email":email, "phone":phone});
    db.session.commit()

    session["username"] = username
    return redirect("/")
    
@app.route("/new_lesson")
def new_lesson():
    return render_template("/new_lesson.html")

@app.route("/new_lesson_create",methods=["POST"])
def new_lesson_create():
    name = request.form["name"]
    spots = request.form["spots"]
    date = request.form["date"]
    start = request.form["start"]
    duration = request.form["duration"]

    sql = "INSERT INTO lessons (name, spots, date, start, duration) VALUES (:name, :spots, :date, :start, :duration)"
    db.session.execute(sql, {"name":name, "spots":spots, "date":date, "start":start, "duration":duration})
    db.session.commit()

    return redirect("/")

@app.route("/sign_up",methods=["POST"])
def sign_up():
    username = session["username"]
    lesson_id = request.form["id"]

    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user_id = result.fetchone()[0]
    
    sql = "INSERT INTO sign_ups (lesson_id, user_id) VALUES (:lesson_id, :user_id)"
    db.session.execute(sql, {"lesson_id":lesson_id, "user_id":user_id})
    db.session.commit()

    flash("Ilmoittautuminen onnistui.")

    return redirect("/")

@app.route("/account")
def account():
    username = session["username"]
    sql = "SELECT first_name, last_name, email, phone FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user_information = result.fetchone()
    
    return render_template("/account.html", user_information=user_information)

@app.route("/account_update",methods=["POST"])
def account_update():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    phone = request.form["phone"]
    username = session["username"]

    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user_id = result.fetchone()[0]

    sql = "UPDATE users SET first_name=:first_name, last_name=:last_name, email=:email, phone=:phone WHERE id=:user_id"
    db.session.execute(sql, {"first_name":first_name, "last_name":last_name, "email":email, "phone":phone, "user_id":user_id})
    db.session.commit()

    flash("Tiedot päivitetty.")

    return render_template("/account.html")