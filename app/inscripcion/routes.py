from app.inscripcion import bp
from flask import render_template

@bp.route('/')
def inscripcion():
    return render_template("index.html")

@bp.route('/preinscripcion')
def preinscripcion():
    return render_template("index.html")