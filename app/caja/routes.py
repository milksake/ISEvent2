from app.caja import bp
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required
from app.extensions import db
from datetime import datetime

############
# CF-12-01 #
############
@bp.route('/')
@bp.route('/<id>')
@login_required
def caja(id = None):
    if id:
        eve = db.Evento.get(id=int(id))
        if not eve:
            flash("Ese evento no existe")
            return redirect(url_for('main.index'))
        return render_template("caja.html", evento=eve)
    return render_template("caja.html", eventos=db.Evento.select())
# FIN

############
# CF-12-02 #
############
@bp.route('/añadirIngreso/<id>', methods=['GET', 'POST'])
@login_required
def añadirIngreso(id):
    eve = db.Evento.get(id=int(id))
    if not eve:
        flash("Ese evento no existe")
        return redirect(url_for('main.index'))
    if request.method == 'POST':
        db.Ingreso(monto=float(request.form['monto']),
                         descripcion=request.form['descripcion'],
                         fecha=datetime.strptime(request.form['fecha'], '%Y-%m-%dT%H:%M'),
                         evento=eve)
        flash('Ingreso añadido')
        return redirect(url_for('caja.caja'))
    return render_template('añadirIngreso.html', title='Ingreso', actividades=eve.actividades)
# FIN

############
# CF-12-03 #
############
@bp.route('/añadirEgreso/<id>', methods=['GET', 'POST'])
@login_required
def añadirEgreso(id):
    eve = db.Evento.get(id=int(id))
    if not eve:
        flash("Ese evento no existe")
        return redirect(url_for('main.index'))
    if request.method == 'POST':
        db.Egreso(monto=float(request.form['monto']),
                       descripcion=request.form['descripcion'],
                       fecha=datetime.strptime(request.form['fecha'], '%Y-%m-%dT%H:%M'),
                       evento=eve)
        flash('Egreso añadido')
        return redirect(url_for('caja.caja'))
    return render_template('añadirIngreso.html', title='Egreso', actividades=eve.actividades)
# FIN