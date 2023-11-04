from app.caja import bp
from flask import render_template

@bp.route('/')
def caja():
    return render_template("index.html")
