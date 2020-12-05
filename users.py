from flask import session, flash
from werkzeug.security import check_password_hash
from db import db

def login(username, password):
    sql = "SELECT password, id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()

    if user is None:
        flash("Käyttäjätunnus tai salasana väärin.")
        return False
    else:
        if check_password_hash(user[0], password):
            session["user_id"] = user[1]
            session["username"] = username
            session["admin"] = False
            if is_admin(user[1]):
                session["admin"] = True
            return True
        else:
            flash("Käyttäjätunnus tai salasana väärin.")
            return False

def logout():
    del session["user_id"]
    try:
        del session["admin"]
    except Exception:
        return

def register(username, hash_value, first_name, last_name, email, phone):
    sql = "SELECT username FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    # Bug: 2 x Flash when creating account with existing username
    if user is None:
        sql = "INSERT INTO users (username, password, first_name, last_name, email, phone) " \
              "VALUES (:username, :password, :first_name, :last_name, :email, :phone)"
        db.session.execute(sql, {"username":username, "password":hash_value,
                                 "first_name":first_name, "last_name":last_name,
                                 "email":email, "phone":phone})
        db.session.commit()
    else:
        flash("Käyttäjänimi varattu. Valitse toinen käyttäjänimi.")
        username = " "
        return login(username, hash_value)

    flash("Käyttäjätunnus luotu. Voit nyt kirjautua sisään.")
    return login(username, hash_value)

def account_information(user_id):
    sql = "SELECT first_name, last_name, email, phone FROM users WHERE id=:user_id"
    result = db.session.execute(sql, {"user_id":user_id})
    return result.fetchone()
    
def account_update(first_name, last_name, email, phone, user_id):
    sql = "UPDATE users SET first_name=:first_name, last_name=:last_name, " \
          "email=:email, phone=:phone WHERE id=:user_id"
    db.session.execute(sql, {"first_name":first_name, "last_name":last_name,
                             "email":email, "phone":phone, "user_id":user_id})
    db.session.commit()

    flash("Tiedot päivitetty.")

def remove_account(user_id):
    if user_id == 5:
        flash("Testikäyttäjää ei voi poistaa.")
        return
    sql = "DELETE FROM users WHERE id=:user_id"
    db.session.execute(sql, {"user_id":user_id})
    db.session.commit()

    flash("Käyttäjätunnus poistettu.")
    
    if session["admin"] == True:
        return

def is_admin(user_id):
    sql = "SELECT admin FROM users WHERE id=:user_id"
    result = db.session.execute(sql, {"user_id":user_id})
    admin = result.fetchone()[0]

    if admin == 1:
        return True

def get_users():
    sql = "SELECT id, username, first_name, last_name, email, phone FROM users"
    result = db.session.execute(sql)
    users = result.fetchall()
    db.session.commit()

    return users

def get_user_id(username):
    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user_id = result.fetchone()[0]

    return user_id

def remove_sign_ups(user_id):
    sql = "DELETE FROM sign_ups WHERE user_id=:user_id"
    db.session.execute(sql, {"user_id":user_id})
    db.session.commit()
