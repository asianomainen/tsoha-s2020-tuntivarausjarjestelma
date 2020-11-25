from flask import flash
from db import db

def get_lessons():
    global all_lessons
    sql = "SELECT L.id, L.name, L.spots-COUNT(S.id), L.date, L.start, L.duration " \
          "FROM lessons L LEFT JOIN sign_ups S ON L.id=S.lesson_id GROUP BY L.id ORDER BY L.date"
    result = db.session.execute(sql)
    all_lessons = result.fetchall()

    return all_lessons

def new_lesson(name, spots, date, start, duration):
    sql = "INSERT INTO lessons (name, spots, date, start, duration)" \
    "VALUES (:name, :spots, :date, :start, :duration)"
    db.session.execute(sql, {"name":name, "spots":spots, "date":date,
                             "start":start, "duration":duration})
    db.session.commit()

def sign_up(user_id, lesson_id):
    if lesson_contains(user_id, lesson_id) == True:
        flash("Olet jo ilmoittautunut tälle tunnille.")
    else:
        if reserve(lesson_id) == False:
            sql = "INSERT INTO sign_ups (lesson_id, user_id) VALUES (:lesson_id, :user_id)"
            db.session.execute(sql, {"lesson_id":lesson_id, "user_id":user_id})
            db.session.commit()

            flash("Ilmoittautuminen onnistui.")

        else:
            sql = "INSERT INTO sign_ups (lesson_id, user_id, reserve) " \
                  "VALUES (:lesson_id, :user_id, 1)"
            db.session.execute(sql, {"lesson_id":lesson_id, "user_id":user_id})
            db.session.commit()

            flash("Ilmoittautuminen varasijalle onnistui.")


def undo_sign_up(user_id, lesson_id):
    if lesson_contains(user_id, lesson_id) == True:
        sql = "DELETE FROM sign_ups WHERE lesson_id=:lesson_id AND user_id=:user_id"
        db.session.execute(sql, {"lesson_id":lesson_id, "user_id":user_id})
        db.session.commit()
        flash("Ilmoittautuminen peruttu.")
    else:
        flash("Et ole ilmoittautunut tälle tunnille.")

def lesson_contains(user_id, lesson_id):
    sql = "SELECT id FROM sign_ups WHERE user_id=:user_id AND lesson_id=:lesson_id"
    result = db.session.execute(sql, {"user_id":user_id, "lesson_id":lesson_id})
    sign_up_id = result.fetchone()

    if sign_up_id is None:
        return False
    return True

def reserve(lesson_id):
    return spots(lesson_id) <= total_participants(lesson_id)

def spots(lesson_id):
    sql = "SELECT spots FROM lessons WHERE id=:lesson_id"
    result = db.session.execute(sql, {"lesson_id":lesson_id})
    spots = result.fetchone()[0]

    return spots

def total_participants(lesson_id):
    sql = "SELECT COUNT(id) FROM sign_ups WHERE lesson_id=:lesson_id"
    result = db.session.execute(sql, {"lesson_id":lesson_id})
    participants = result.fetchone()[0]

    return participants

def lesson_information(lesson_id):
    sql = "SELECT name, spots, date, start, duration FROM lessons WHERE id=:lesson_id"
    result = db.session.execute(sql, {"lesson_id":lesson_id})
    return result.fetchone()

def lesson_update(name, spots, date, start, duration, lesson_id):
    sql = "UPDATE lessons SET name=:name, spots=:spots, " \
          "date=:date, start=:start, duration=:duration WHERE id=:lesson_id"
    db.session.execute(sql, {"name":name, "spots":spots, "date":date, "start":start,
                             "duration":duration, "lesson_id":lesson_id})
    db.session.commit()

    flash("Tiedot päivitetty.")

def remove_lesson(lesson_id):
    sql = "DELETE FROM lessons WHERE id=:lesson_id"
    db.session.execute(sql, {"lesson_id":lesson_id})
    db.session.commit()

    flash("Tunti poistettu.")

def get_participants(lesson_id):
    sql = "SELECT A.id, username, first_name, last_name, email, phone " \
          "FROM users A LEFT JOIN sign_ups B ON A.id=B.user_id WHERE B.lesson_id=:lesson_id"
    result = db.session.execute(sql, {"lesson_id":lesson_id})
    participants = result.fetchall()
    db.session.commit()

    return participants

def remove_participant(user_id, lesson_id):
    sql = "DELETE FROM sign_ups WHERE user_id=:user_id AND lesson_id=:lesson_id"
    db.session.execute(sql, {"user_id":user_id, "lesson_id":lesson_id})
    db.session.commit()

    flash("Käyttäjä poistettu tunnilta.")
