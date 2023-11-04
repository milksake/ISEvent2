from app.gestion import bp
from flask import render_template, abort, request, flash, redirect, url_for
from flask_login import current_user, login_required
from app.models.cuenta import obtenerCuenta, get_user

@bp.route('/', methods=['GET', 'POST'])
@login_required
def gestion():
    if not current_user.rol == "admin":
        abort(403)
    if request.method == "POST":
        for k, v in request.form.lists():
            if v[0] != "no":
                get_user(k).rol = v[0]
        flash("Roles actualizados")
        return redirect(url_for("main.index"))
    cuentas = obtenerCuenta(request.args.get("query", default=""))
    newCuentas = []
    for x in cuentas:
        if x.id != current_user.id:
            newCuentas.append(x)
    return render_template("rolUI.html", cuentas=newCuentas)
