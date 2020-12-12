from flask import flash
from db import db

def get_lessons():
    global all_lessons
    sql = "SELECT L.id, L.name, L.date, L.starts, L.ends, L.spots-COUNT(S.id) " \
          "FROM lessons L LEFT JOIN sign_ups S ON L.id=S.lesson_id " \
          "WHERE (L.date + L.starts) > CURRENT_TIMESTAMP GROUP BY L.id ORDER BY L.date"
    result = db.session.execute(sql)
    all_lessons = result.fetchall()

    return all_lessons

def new_lesson(name, spots, date, starts, ends):
    sql = "INSERT INTO lessons (name, spots, date, starts, ends)" \
    "VALUES (:name, :spots, :date, :starts, :ends)"
    db.session.execute(sql, {"name":name, "spots":spots, "date":date,
                             "starts":starts, "ends":ends})
    db.session.commit()

def sign_up(user_id, lesson_id):
    if lesson_contains_user(user_id, lesson_id) == True:
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
    if lesson_contains_user(user_id, lesson_id) == True:
        sql = "SELECT id FROM lessons WHERE " \
              "(date + starts) > CURRENT_TIMESTAMP + interval '12 hour' AND id=:lesson_id"
        result = db.session.execute(sql, {"lesson_id":lesson_id})
        try:
            lesson = result.fetchone()[0]

            if lesson == lesson_id:
                sql = "DELETE FROM sign_ups WHERE lesson_id=:lesson_id AND user_id=:user_id"
                db.session.execute(sql, {"lesson_id":lesson_id, "user_id":user_id})
                db.session.commit()
                flash("Ilmoittautuminen peruttu.")
        except:
            flash("Tunnin alkuun on alle 12h. Et voi valitettavasti enää perua osallistumista.")
    else:
        flash("Et ole ilmoittautunut tälle tunnille.")

def lesson_contains_user(user_id, lesson_id):
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
    sql = "SELECT name, spots, date, starts, ends FROM lessons WHERE id=:lesson_id"
    result = db.session.execute(sql, {"lesson_id":lesson_id})
    return result.fetchone()

def lesson_update(name, spots, date, starts, ends, lesson_id):
    sql = "UPDATE lessons SET name=:name, spots=:spots, " \
          "date=:date, starts=:starts, ends=:ends WHERE id=:lesson_id"
    db.session.execute(sql, {"name":name, "spots":spots, "date":date, "starts":starts,
                             "ends":ends, "lesson_id":lesson_id})
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

def get_user_lessons(user_id):
    sql = "SELECT L.id, L.name, L.date, L.starts, L.ends FROM " \
    "lessons L LEFT JOIN sign_ups S ON L.id=S.lesson_id  WHERE S.user_id=:user_id"
    result = db.session.execute(sql, {"user_id":user_id})
    all_user_lessons = result.fetchall()
 
    return all_user_lessons
