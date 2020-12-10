from flask import flash
from db import db

def feedback(identifier, message):
    try:
        sql = "INSERT INTO messages (user_id, message) VALUES (:identifier, :message)"
        db.session.execute(sql, {"identifier":identifier, "message":message})
    except:
        sql = "INSERT INTO messages (email, message) VALUES (:identifier, :message)"
        db.session.execute(sql, {"identifier":identifier, "message":message})
    db.session.commit()
    flash("Kiitos palautteestasi")