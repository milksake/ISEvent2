from app.gestion import bp
from flask import render_template, abort, request, flash, redirect, url_for
from flask_login import current_user, login_required
from app.extensions import db

############
# CF-13-01 #
############
@bp.route('/roles', methods=['GET', 'POST'])
@login_required
def roles():
    if not current_user.rol == "admin":
        abort(403)
    if request.method == "POST":
        for k, v in request.form.lists():
            if v[0] != "no":
                db.Cuenta.get(nombre=k).rol = v[0]
        flash("Roles actualizados")
        return redirect(url_for("main.index"))
    cuentas = db.Cuenta.select(lambda c: request.args.get("query", default="") in c.nombre and c.id != current_user.id)
    return render_template("rolUI.html", cuentas=cuentas)
# FIN

############
# CF-13-05 #
############
@bp.route('/comite/<id>')
@bp.route('/comite')
@login_required
def comites(id = None):
    if current_user.rol != "admin":
        abort(403)
    if id:
        comit = db.Comite.get(id=int(id))
        if not comit:
            flash("Ese comité no existe")
            return redirect(url_for('main.index'))
        return render_template('comiteUI.html', comite=comit)
    comits = db.Comite.select()
    return render_template('comiteUI.html', comites=comits)
# FIN

############
# CF-13-03 #
############
@bp.route('/añadirComite', methods=['GET', 'POST'])
@login_required
def añadirComite():
    if current_user.rol != "admin":
        abort(403)
    if request.method == 'POST':
        cuentas = db.Cuenta.select(lambda c : c.nombre in request.form.getlist('cuentasA'))
        c = db.Comite(
            nombre = request.form['nombre'],
            cuentas = cuentas
        )
        flash("Comité creado")
        return redirect(url_for('gestion.comites', id=c.id))
    return render_template('añadirComite.html')
# FIN

############
# CF-13-04 #
############
@bp.route('/modificarComite/<id>', methods=['GET', 'POST'])
@login_required
def modificarComite(id):
    if current_user.rol != "admin":
        abort(403)
    comit = db.Comite.get(id=int(id))
    if not comit:
        flash("No existe ese comite")
        return redirect(url_for('gestion.comites'))
    if request.method == 'POST':
        cuentasAdd = db.Cuenta.select(lambda c : c.nombre in request.form.getlist('cuentasA'))
        cuentasErase = [int(i) for i in request.form.getlist('cuentasE')]
        print(cuentasErase)
        cuentasErase = db.Cuenta.select(lambda c: c.id in cuentasErase)
        comit.nombre = request.form['nombre']
        comit.cuentas.remove(cuentasErase)
        comit.cuentas.add(cuentasAdd)
        flash("Comité modificado")
        return redirect(url_for('gestion.comites', id=comit.id))
    return render_template('añadirComite.html', comite=comit)
# FIN