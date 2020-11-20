from db import db
from flask import flash


def get_lessons():
    global all_lessons
    sql = "SELECT id, name, spots, date, start, duration FROM lessons"
    result = db.session.execute(sql)
    all_lessons = result.fetchall()
    return all_lessons

def new_lesson(name, spots, date, start, duration):
    sql = "INSERT INTO lessons (name, spots, date, start, duration)" \
    "VALUES (:name, :spots, :date, :start, :duration)"
    db.session.execute(sql, {"name":name, "spots":spots, "date":date,
                             "start":start, "duration":duration})
    db.session.commit()

def sign_up(username, lesson_id):
    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user_id = result.fetchone()[0]

    sql = "INSERT INTO sign_ups (lesson_id, user_id) VALUES (:lesson_id, :user_id)"
    db.session.execute(sql, {"lesson_id":lesson_id, "user_id":user_id})
    db.session.commit()

    flash("Ilmoittautuminen onnistui.")

def undo_sign_up(username, lesson_id):
    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user_id = result.fetchone()[0]

    sql = "DELETE FROM sign_ups WHERE lesson_id=:lesson_id AND user_id=:user_id"
    db.session.execute(sql, {"lesson_id":lesson_id, "user_id":user_id})
    db.session.commit()

    flash("Ilmoittautuminen peruttu.")