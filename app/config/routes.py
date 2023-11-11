from app.config import bp
from flask import render_template, request, flash, redirect, url_for, abort
from flask_login import login_required, current_user
from app.models.material import Material, materialesList
from app.extensions import db

@bp.route('/eventos')
def eventos():
    return render_template("index.html")

@bp.route('/ambientes')
def ambientes():
    amb = db.Ambiente.select(lambda a : True)
    return render_template("ambienteUI.html", ambientes=amb)

@bp.route('/añadirAmbiente', methods=['GET', 'POST'])
def añadirAmbiente():
    if request.method == 'POST':
        db.Ambiente(nombre=request.form['nombre'],
                    aforo=request.form['aforo'],
                    descripcion=request.form['descripcion'],
                    imagen=request.form['imagen'])
        flash("Ambiente agregado")
        return redirect(url_for('config.ambientes'))
    return render_template("añadirAmbiente.html")

@bp.route('/modificarAmbientes/<id>', methods=['GET','POST'])
def modificarAmbiente(id):
    if request.method == 'POST':
        amb = db.Ambiente.get(int(id))
        if not amb:
            flash("No existe ese ambiente")
            return redirect(url_for('main.index'))
        db.Ambiente(nombre=request.form['nombre'],
                    aforo=request.form['aforo'],
                    descripcion=request.form['descripcion'],
                    imagen=request.form['imagen'])
        flash("Ambiente modificado")
        return redirect(url_for('config.ambientes'))
    return render_template("añadirAmbiente.html")

@bp.route('/actividades')
def actividades():
    return render_template("index.html")

@login_required
@bp.route('/materiales')
def materiales():
    #if current_user.rol != "admin":
    #    abort(403)
    return render_template("materialUI.html", materiales=materialesList)

@bp.route('/añadirMaterial', methods=['GET', 'POST'])
@login_required
def añadirMaterial():
    #if current_user.rol != "admin":
    #    abort(403)
    if request.method == 'POST':
        materialesList.append(Material(len(materialesList), request.form['nombre'], request.form['cantidad'], request.form['descripcion'], None))
        flash("Material Creado")
        return redirect(url_for('config.materiales'))
    return render_template("añadirMaterial.html")

@bp.route('/modificarMaterial/<id>', methods=['GET', 'POST'])
@login_required
def modificarMaterial(id):
    #if current_user.rol != "admin":
    #    abort(403)
    if request.method == 'POST':
        materialesList[int(id)] = Material(int(id), request.form['nombre'], request.form['cantidad'], request.form['descripcion'], None)
        flash("Material Modificado")
        return redirect(url_for('config.materiales'))
    return render_template("añadirMaterial.html")