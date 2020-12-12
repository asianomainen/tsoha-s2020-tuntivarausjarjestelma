from flask import flash
from db import db

def feedback(user_id, message):
    sql = "INSERT INTO messages (user_id, message) VALUES (:user_id, :message)"
    db.session.execute(sql, {"user_id":user_id, "message":message})
    db.session.commit()
    flash("Kiitos palautteestasi")

def anonymous_feedback(email, message):
    sql = "INSERT INTO messages (email, message) VALUES (:email, :message)"
    db.session.execute(sql, {"email":email, "message":message})
    db.session.commit()
    flash("Kiitos palautteestasi")