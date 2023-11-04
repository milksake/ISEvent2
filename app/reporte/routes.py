from app.reporte import bp
from flask import render_template

@bp.route('/')
def reporte():
    return render_template("index.html")
