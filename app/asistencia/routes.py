from app.asistencia import bp
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required
from app.extensions import db
from pony.orm import select, commit

@bp.route('/')
@bp.route('/<id>', methods=['GET', 'POST'])
@login_required
def asistencia(id = None):
    if not id:
        eves = db.Evento.select()
        return render_template("asistenciaUI.html", eventos=eves)
    act = db.Actividad.get(id=int(id))
    if not act:
        flash("Esa actividad no existe.")
        return redirect(url_for('main.index'))
    if request.method == 'POST':
        ins_id = request.form.getlist('asistencia')
        for in_id in ins_id:
            toUP = db.Inscripcion.get(id=int(in_id))
            if toUP:
                toUP.asistencias.add(act)
        flash('Asistencia guardada')
        return redirect(url_for('main.index'))

    ins = select(i for i in db.Inscripcion if int(id) in i.asistencias.id)
    ins = select((i, (i in ins)) for i in db.Inscripcion if int(id) in i.paquete.actividades.id)
    for p in ins:
        print(p)
    return render_template("asistenciaUI.html", inscripciones=ins, nombreActividad=act.nombre)

@bp.route('/materiales')
@bp.route('/materiales/<id>', methods=['GET', 'POST'])
def entrega(id = None):
    if not id:
        eves = db.Evento.select()
        return render_template("entrega.html", eventos=eves)
    
    act = db.Actividad.get(id=int(id))
    if not act:
        flash("Esa actividad no existe.")
        return redirect(url_for('main.index'))
    if request.method == 'POST':
        mensaje = ""
        for k, v in request.form.lists():
            if v[0] != "0":
                material = db.Material.get(id=int(k))
                if material.cantidad > int(v[0]):
                    material.cantidad -= int(v[0])
                else:
                    mensaje += f"No se pudo entregar {int(v[0]) - material.cantidad} del material {material.nombre}. "
                    material.cantidad = 0
        if len(mensaje) == 0:
            mensaje += "Materiales Entregados"
        flash(mensaje)
        #redirect(url_for('asistencia.entrega', id=act.id))
        commit()
    
    return render_template("entrega.html", nombreActividad=act.nombre, materiales=act.materiales)

