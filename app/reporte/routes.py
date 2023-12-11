from app.reporte import bp
from flask import render_template, request, flash, url_for, redirect
from flask_login import current_user, login_required
from app.extensions import db
from pony.orm import group_concat
from datetime import datetime

@bp.route('/')
def reporte():
    return render_template("index.html")

@bp.route('/inscritos/')
@bp.route('/inscritos/<id>')
@login_required
def reporteInscritos(id = None):
    if not id:
        eves = db.Evento.select()
        return render_template("reporteInscritos.html", eventos=eves)
    eve = db.Evento.get(id=int(id))
    if not eve:
        flash("Ese evento no existe.")
        return redirect(url_for('main.index'))
    #ins = db.Inscripcion.select(lambda c: request.args.get("query", default="") in c.nombre and c.id != current_user.id)
    ins = db.Inscripcion.select(lambda i: i.paquete.evento.id == id)
    rol = request.args.get('rol')
    if rol and rol != "None":
        ins = ins.filter(lambda i : i.paquete.rol == rol)
    actividades = request.args.get('actividades')
    if actividades and actividades != "None":
        ins = ins.filter(lambda i : group_concat((a.nombre for a in i.paquete.actividades), sep=', ') == actividades)
    fechaIni = request.args.get('fechaIni')
    if fechaIni and fechaIni != "":
        ins = ins.filter(lambda i : i.fecha >= datetime.strptime(fechaIni, '%Y-%m-%dT%H:%M'))
    fechaFin = request.args.get('fechaFin')
    if fechaFin and fechaFin != "":
        ins = ins.filter(lambda i : i.fecha <= datetime.strptime(fechaFin, '%Y-%m-%dT%H:%M'))
    return render_template("reporteInscritos.html", inscripciones=ins, evento=eve)