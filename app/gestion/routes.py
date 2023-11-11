from app.gestion import bp
from flask import render_template, abort, request, flash, redirect, url_for
from flask_login import current_user, login_required
from app.extensions import db
#CF-13-01
@bp.route('/', methods=['GET', 'POST'])
@login_required
def gestion():
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
