from app.inscripcion import bp
from flask import render_template, redirect, flash, url_for, request
from flask_login import login_required, current_user
from app.extensions import db
from datetime import datetime

############
# CF-04-01 #
############
@bp.route('/evento/<id>')
def evento(id):
    '''
        Mostrar la interfaz de un evento con sus detalles
    '''
    eve = db.Evento.get(id=int(id))
    if (not eve):
        flash("Ese evento no existe")
        return redirect(url_for("main.index"))
    return render_template("eventoUI.html", evento=eve, fechaActual=datetime.now().replace(second=0, microsecond=0))
# FIN

############
# CF-04-02 #
############
@bp.route('/<id>', methods=['GET', 'POST'])
@login_required
def inscripcion(id):
    '''
        Inscribirse a un evento
    '''
    eve = db.Evento.get(id=int(id))
    if (not eve):
        flash("Ese evento no existe")
        return redirect(url_for("main.index"))
    if request.method == 'POST':
        paq = db.Paquete[request.form['paquete']]
        nowDateTime = datetime.now().replace(second=0, microsecond=0)
        ing = db.Ingreso(monto=float(paq.precio),
                   descripcion=f"Inscripcion: {current_user.nombre}",
                   fecha=nowDateTime,
                   evento=eve)
        db.Inscripcion(documentoId = request.form['docId'],
                       paquete = paq,
                       cuenta = current_user,
                       fecha = nowDateTime,
                       preinscripcion = False,
                       ingreso=ing)
        flash('Inscripcion completa')
        return redirect(url_for('inscripcion.evento', id=eve.id))
    return render_template("inscripcion.html", evento=eve)
# FIN

############
# CF-05-01 #
############
@bp.route('/preinscripcion/<id>', methods=['GET', 'POST'])
def preinscripcion(id):
    '''
        Preinscribirse a un evento
    '''
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
                            fecha = datetime.now().replace(second=0, microsecond=0),
                            preinscripcion = True)
        else:
            db.Inscripcion(documentoId = request.form['docId'],
                            paquete = paq,
                            fecha = datetime.now().replace(second=0, microsecond=0),
                            nombres = request.form['nombres'],
                            apellidos = request.form['apellidos'],
                            correo = request.form['correo'],
                            preinscripcion = True)
        flash('Preinscripcion completa')
        return redirect(url_for('inscripcion.evento', id=eve.id))
    return render_template("preinscripcion.html", evento=eve)
# FIN