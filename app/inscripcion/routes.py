from app.inscripcion import bp
from flask import render_template, redirect, flash, url_for, request
from flask_login import login_required, current_user
from app.extensions import db

@bp.route('/evento/<id>')
def evento(id):
    eve = db.Evento.get(id=int(id))
    if (not eve):
        flash("Ese evento no existe")
        return redirect(url_for("main.index"))
    return render_template("eventoUI.html", evento=eve)

@bp.route('/<id>', methods=['GET', 'POST'])
@login_required
def inscripcion(id):
    eve = db.Evento.get(id=int(id))
    if (not eve):
        flash("Ese evento no existe")
        return redirect(url_for("main.index"))
    if request.method == 'POST':
        paq = db.Paquete[request.form['paquete']]
        db.Inscripcion(documentoId = request.form['docId'],
                       paquete = paq,
                       cuenta = current_user)
        flash('Inscripcion completa')
        return redirect(url_for('inscripcion.evento', id=eve.id))
    return render_template("inscripcion.html", evento=eve)

@bp.route('/preinscripcion')
def preinscripcion():
    return render_template("index.html")