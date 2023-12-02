from app.inscripcion import bp
from flask import render_template, redirect, flash, url_for, request
from flask_login import login_required, current_user
from app.extensions import db
from datetime import datetime

@bp.route('/evento/<id>')
def evento(id):
    eve = db.Evento.get(id=int(id))
    if (not eve):
        flash("Ese evento no existe")
        return redirect(url_for("main.index"))
    return render_template("eventoUI.html", evento=eve, fechaActual=datetime.now())

@bp.route('/<id>', methods=['GET', 'POST'])
@login_required
def inscripcion(id):
    eve = db.Evento.get(id=int(id))
    if (not eve):
        flash("Ese evento no existe")
        return redirect(url_for("main.index"))
    if request.method == 'POST':
        paq = db.Paquete[request.form['paquete']]
        nowDateTime = datetime.now()
        ing = db.Ingreso(monto=int(paq.precio),
                   descripcion="inscripcion",
                   fecha=nowDateTime)
        db.Inscripcion(documentoId = request.form['docId'],
                       paquete = paq,
                       cuenta = current_user,
                       fecha = nowDateTime,
                       preinscripcion = False,
                       ingreso=ing)
        flash('Inscripcion completa')
        return redirect(url_for('inscripcion.evento', id=eve.id))
    return render_template("inscripcion.html", evento=eve)

@bp.route('/preinscripcion/<id>', methods=['GET', 'POST'])
def preinscripcion(id):
    eve = db.Evento.get(id=int(id))
    if (not eve):
        flash("Ese evento no existe")
        return redirect(url_for("main.index"))
    if request.method == 'POST':
        paq = db.Paquete[request.form['paquete']]
        if current_user.is_authenticated:
            db.Inscripcion(documentoId = request.form['docId'],
                            paquete = paq,
                            cuenta = current_user,
                            fecha = datetime.now(),
                            preinscripcion = True)
        else:
            db.Inscripcion(documentoId = request.form['docId'],
                            paquete = paq,
                            fecha = datetime.now(),
                            nombres = request.form['nombres'],
                            apellidos = request.form['apellidos'],
                            correo = request.form['correo'],
                            preinscripcion = True)
        flash('Preinscripcion completa')
        return redirect(url_for('inscripcion.evento', id=eve.id))
    return render_template("preinscripcion.html", evento=eve)