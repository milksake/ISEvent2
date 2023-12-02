from app.caja import bp
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required
from app.extensions import db

@bp.route('/')
@login_required
def caja():
    ing = db.Ingreso.select(lambda i: True)
    eg = db.Egreso.select(lambda e: True)
    return render_template("caja.html", ingresos=ing, egresos=eg)

@bp.route('/añadirIngreso', methods=['GET', 'POST'])
@login_required
def añadirIngreso():
    if request.method == 'POST':
        db.Ingreso(monto=int(request.form['monto']),
                         descripcion=request.form['descripcion'],
                         fecha=request.form['fecha'])
        flash('Ingreso añadido')
        return redirect(url_for('caja.caja'))
    return render_template('añadirIngreso.html', title='Ingreso')

@bp.route('/añadirEgreso', methods=['GET', 'POST'])
@login_required
def añadirEgreso():
    if request.method == 'POST':
        db.Egreso(monto=int(request.form['monto']),
                       descripcion=request.form['descripcion'],
                       fecha=request.form['fecha'])
        flash('Egreso añadido')
        return redirect(url_for('caja.caja'))
    return render_template('añadirIngreso.html', title='Egreso')
