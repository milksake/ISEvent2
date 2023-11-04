from app.config import bp
from flask import render_template

@bp.route('/eventos')
def eventos():
    return render_template("index.html")

@bp.route('/ambientes')
def ambientes():
    return render_template("index.html")

@bp.route('/actividades')
def actividades():
    return render_template("index.html")

@bp.route('/materiales')
def materiales():
    return render_template("index.html")