from flask import flash
from db import db

def send_feedback(message, user_id):
    sql = "INSERT INTO feedback (user_id, message) VALUES (:user_id, :message)"
    db.session.execute(sql, {"user_id":user_id, "message":message})
    db.session.commit()
    flash("Kiitos palautteestasi")