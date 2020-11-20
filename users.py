from db import db
from flask import session, flash
from werkzeug.security import check_password_hash

def login(username, password):
    sql = "SELECT password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if user is None:
        flash("Käyttäjätunnus tai salasana väärin.")
        return False
    else:
        hash_value = user[0]
        if check_password_hash(hash_value, password):
            session["username"] = username
            return True
        else:
            return False

def logout():
    del session["username"]

def register(username, password, first_name, last_name, email, phone):
    sql = "SELECT username FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()

    # Bug: 2 x Flash when creating account with existing username

    if user is None:
        sql = "INSERT INTO users (username, password, first_name, last_name, email, phone) " \
              "VALUES (:username, :password, :first_name, :last_name, :email, :phone)"
        db.session.execute(sql, {"username":username, "password":password, "first_name":first_name,
                                "last_name":last_name, "email":email, "phone":phone})
        db.session.commit()
    else:
        flash("Käyttäjänimi varattu. Valitse toinen käyttäjänimi.")
        username = " "
        return login(username,password)

    flash("Käyttäjätunnus luotu. Voit nyt kirjautua sisään.")
    return login(username,password)

def account_information(username):
    sql = "SELECT first_name, last_name, email, phone FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    return result.fetchone()
    
def account_update(first_name, last_name, email, phone, username):
    sql = "UPDATE users SET first_name=:first_name, last_name=:last_name, " \
          "email=:email, phone=:phone WHERE username=:username"
    db.session.execute(sql, {"first_name":first_name, "last_name":last_name,
                             "email":email, "phone":phone, "username":username})
    db.session.commit()

    flash("Tiedot päivitetty.")

def remove_account(username):
    if username == "testi":
        flash("Testikäyttäjää ei voi poistaa")
        return redirect("/account")

    sql = "DELETE FROM users WHERE username=:username"
    db.session.execute(sql, {"username":username})
    db.session.commit()

    flash("Käyttäjätunnus poistettu.")

    logout()

# def is_admin():
#     sql = "SELECT admin FROM users WHERE username=:username"
#     result = db.session.execute(sql, {"username":username})
#     admin = result.fetchone()
#     return admin