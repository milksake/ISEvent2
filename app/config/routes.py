from app.config import bp
from flask import render_template, request, flash, redirect, url_for, abort
from flask_login import login_required, current_user
from app.extensions import db

@bp.route('/eventos')
@login_required
def eventos():
    even = db.Evento.select(lambda e : True)
    return render_template("index.html", eventos=even)

@bp.route('/añadirEvento', methods=['GET', 'POST'])
@login_required
def añadirEvento():
    if request.method == 'POST':
        db.Evento(nombre=request.form['nombre'],
                    descripcion=request.form['descripcion'],
                    fechaInicio=request.form['fechaInicio'],
                    fechaFin=request.form['fechaFin'],
                    imagen=request.form['imagen'],
                    tipo=request.form['tipo'])
        flash("Evento agregado")
        return redirect(url_for('config.eventos'))
    return render_template("añadirEvento.html")

@bp.route('/modificarEvento/<id>', methods=['GET','POST'])
@login_required
def modificarEvento(id):
    if request.method == 'POST':
        ev = db.Evento.get(id=int(id))
        if not ev:
            flash("No existe ese evento")
            return redirect(url_for('main.index'))
        ev.nombre = request.form['nombre']
        ev.descripcion=request.form['descripcion']
        ev.fechaInicio=request.form['fechaInicio']
        ev.fechaFin=request.form['fechaFin']
        ev.imagen=request.form['imagen']
        ev.tipo=request.form['tipo']
        flash("Evento modificado")
        return redirect(url_for('config.eventos'))
    return render_template("añadirEvento.html")

@bp.route('/ambientes')
@login_required
def ambientes():
    amb = db.Ambiente.select(lambda a : True)
    return render_template("ambienteUI.html", ambientes=amb)

@bp.route('/añadirAmbiente', methods=['GET', 'POST'])
@login_required
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
@login_required
def modificarAmbiente(id):
    if request.method == 'POST':
        amb = db.Ambiente.get(id=int(id))
        if not amb:
            flash("No existe ese ambiente")
            return redirect(url_for('main.index'))
        amb.nombre = request.form['nombre']
        amb.aforo = request.form['aforo']
        amb.descripcion = request.form['descripcion']
        amb.imagen = request.form['imagen']
        flash("Ambiente modificado")
        return redirect(url_for('config.ambientes'))
    return render_template("añadirAmbiente.html")

@bp.route('/actividades')
def actividades():
    return render_template("index.html")

@bp.route('/materiales')
@login_required
def materiales():
    #if current_user.rol != "admin":
    #    abort(403)
    mat = db.Material.select(lambda m : True)
    return render_template("materialUI.html", materiales=mat)

@bp.route('/añadirMaterial', methods=['GET', 'POST'])
@login_required
def añadirMaterial():
    #if current_user.rol != "admin":
    #    abort(403)
    if request.method == 'POST':
        db.Material(nombre=request.form['nombre'],
                    cantidad=request.form['cantidad'],
                    tipo=request.form['tipo'])
        flash("Material Creado")
        return redirect(url_for('config.materiales'))
    return render_template("añadirMaterial.html")

@bp.route('/modificarMaterial/<id>', methods=['GET', 'POST'])
@login_required
def modificarMaterial(id):
    #if current_user.rol != "admin":
    #    abort(403)
    if request.method == 'POST':
        mat = db.Event.get(id=int(id))
        mat.nombre = request.form['nombre']
        mat.cantidad = request.form['cantidad']
        mat.tipo = request.form['tipo']
        flash("Material Modificado")
        return redirect(url_for('config.materiales'))
    return render_template("añadirMaterial.html")