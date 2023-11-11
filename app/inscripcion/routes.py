from app.inscripcion import bp
from flask import render_template, redirect, flash, url_for
from app.extensions import db

@bp.route('/evento/<id>')
def evento(id):
    eve = db.Evento.get(id=int(id))
    if (not eve):
        flash("Ese evento no existe")
        return redirect(url_for("main.index"))
    return render_template("eventoUI.html", evento=eve)

@bp.route('/')
def inscripcion():
    return render_template("index.html")

@bp.route('/preinscripcion')
def preinscripcion():
    return render_template("index.html")