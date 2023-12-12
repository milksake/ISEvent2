from app.config import bp
from flask import render_template, request, flash, redirect, url_for, abort
from flask_login import login_required, current_user
from app.extensions import db
from datetime import datetime
from app.forms.FormValidarActividad import FormValidarActividad
from pony.orm import commit

#CF-03-01
@bp.route('/eventos')
@login_required
def eventos():
    even = db.Evento.select()
    return render_template("index.html", eventos=even)

#CF-03-02
@bp.route('/añadirEvento', methods=['GET', 'POST'])
@login_required
def añadirEvento():
    if request.method == 'POST':
        file = request.files['imagen']
        if not file or file.filename == '' or file.filename.split('.')[-1].lower() not in ['jpg', 'png', 'jpeg']:
            flash('Seleccione una imágen valida')
            return redirect(url_for('main.index'))
        nom = request.form['nombre']
        ev = db.Evento.get(nombre=nom)
        if ev:
            flash('Ese nombre de evento ya existe')
            return redirect(url_for('main.index'))
        comit = db.Comite.get(id=int(request.form['comite']))
        if not comit:
            flash('Ese comite no es válido')
        
        newEve = db.Evento(
            nombre=nom,
            descripcion=request.form['descripcion'],
            fechaInscripcionInicio=datetime.strptime(request.form['fechaInscripcionIni'], '%Y-%m-%dT%H:%M'),
            fechaInscripcionFin=datetime.strptime(request.form['fechaInscripcionFin'], '%Y-%m-%dT%H:%M'),
            tipo=request.form['tipo'],
            comite=comit
        )
        commit()
        file.save("./app/" + url_for('static', filename=f"imgs/eventos/{ev.id}.png"))
        flash("Evento agregado")
        return redirect(url_for('config.eventos'))
    comits = db.Comite.select()
    return render_template("añadirEvento.html", comites=comits)

#CF-03-03
@bp.route('/modificarEvento/<id>', methods=['GET','POST'])
@login_required
def modificarEvento(id):
    ev = db.Evento.get(id=int(id))
    if not ev:
        flash("No existe ese evento")
        return redirect(url_for('main.index'))
    if request.method == 'POST':
        nom = request.form['nombre']
        ev1 = db.Evento.get(nombre=nom)
        if ev1 and ev1.nombre != ev.nombre:
            flash('Ese nombre de evento ya existe')
            return redirect(url_for('main.index'))
        comit = db.Comite.get(id=int(request.form['comite']))
        if not comit:
            flash('Ese comite no es válido')

        ev.nombre = request.form['nombre']
        ev.descripcion=request.form['descripcion']
        ev.fechaInscripcionInicio=datetime.strptime(request.form['fechaInscripcionIni'], '%Y-%m-%dT%H:%M')
        ev.fechaInscripcionFin=datetime.strptime(request.form['fechaInscripcionFin'], '%Y-%m-%dT%H:%M')
        ev.tipo=request.form['tipo']
        ev.comite = comit

        file = request.files['imagen']
        if file and file.filename != '' and file.filename.split('.')[-1].lower() in ['jpg', 'png', 'jpeg']:
            file.save("./app/" + url_for('static', filename=f"imgs/eventos/{ev.id}.png"))

        flash("Evento modificado")
        return redirect(url_for('config.eventos'))
    comits = db.Comite.select()
    return render_template("añadirEvento.html", evento=ev, comites=comits)

@bp.route('/paquetes')
@bp.route('/paquetes/<id>')
@login_required
def paquetes(id=None):
    if not id:
        evess = db.Evento.select(lambda e : True)
        return render_template("paqueteUI.html", eventos=evess)
    eve = db.Evento.get(id=int(id))
    if (not eve):
        flash("Ese evento no existe")
        return redirect(url_for("main.index"))
    return render_template("paqueteUI.html", evento=eve)

@bp.route('/añadirPaquete/<id>', methods=['GET', 'POST'])
@login_required
def añadirPaquete(id = None):
    eve = db.Evento.get(id=int(id))
    if not eve:
        flash("No existe ese evento")
        return redirect(url_for('main.index'))
    if request.method == 'POST':
        acts_id = request.form.getlist('actividades')
        if len(acts_id) == 0:
            flash("Se tiene que elegir al menos una actividad")
            return redirect(url_for('main.index'))
        acts_id = [int(a) for a in acts_id]
        acts = db.Actividad.select(lambda a: a.id in acts_id)
        db.Paquete(
            precio = int(request.form['precio']),
            rol = request.form['rol'],
            evento = eve,
            actividades = acts,
        )
        flash("Paquete añadido")
        return redirect(url_for('config.paquetes', id=id))
    return render_template("añadirPaquete.html", evento=eve)

@bp.route('/modificarPaquete/<id>', methods=['GET', 'POST'])
@login_required
def modificarPaquete(id):
    paq = db.Paquete.get(id=int(id))
    if not paq:
        flash("No existe ese paquete")
        return redirect(url_for('main.index'))
    if request.method == 'POST':
        acts_id = request.form.getlist('actividades')
        if len(acts_id) == 0:
            flash("Se tiene que elegir al menos una actividad")
            return redirect(url_for('main.index'))
        acts_id = [int(a) for a in acts_id]
        acts = db.Actividad.select(lambda a: a.id in acts_id)
        paq.precio = int(request.form['precio'])
        paq.rol = request.form['rol']
        paq.actividades = acts
        flash("Paquete modificado")
        return redirect(url_for('config.paquetes', id=paq.evento.id))
    return render_template("añadirPaquete.html", evento=paq.evento)

#CF-20-01
@bp.route('/ambientes')
@login_required
def ambientes():
    amb = db.Ambiente.select(lambda a : True)
    return render_template("ambienteUI.html", ambientes=amb)
#CF-20-02
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
#CF-20-03
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

#CF-18-01
@bp.route('/materiales')
@login_required
def materiales():
    #if current_user.rol != "admin":
    #    abort(403)
    mat = db.Material.select(lambda m : True)
    return render_template("materialUI.html", materiales=mat)
#CF-18-02
@bp.route('/añadirMaterial', methods=['GET', 'POST'])
@login_required
def añadirMaterial():
    #if current_user.rol != "admin":
    #    abort(403)
    if request.method == 'POST':
        eg = db.Egreso(monto=int(request.form['costo']),
                       descripcion="material",
                       fecha=datetime.now())
        db.Material(nombre=request.form['nombre'],
                    cantidad=request.form['cantidad'],
                    tipo=request.form['tipo'],
                    egreso=eg)
        flash("Material Creado")
        return redirect(url_for('config.materiales'))
    return render_template("añadirMaterial.html")
#CF-18-03
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


#---------------------------INICIO ACTIVIDADES-----------------------------------------------------------
#CF-17-01
@bp.route('/actividades')
@login_required
def actividades():
    act = db.Actividad.select(lambda a : True)
    return render_template("actividadUI.html", actividades=act) #variable de template
#CF-17-02
@bp.route('/añadirActividad', methods=['GET', 'POST'])
@login_required
def añadirActividad():
    form = FormValidarActividad()
    if request.method == 'POST' and form.validate():
        nombre = form.nombre.data
        fechaInicio= datetime.combine(form.fechaInicio.data, datetime.min.time())
        fechaFin= datetime.combine(form.fechaFin.data, datetime.min.time())
        tipo = form.tipo.data
        imagen= form.imagen.data
        descripcion = form.descripcion.data
        evento= form.evento.data
        ambiente= form.ambiente.data
        #aniadiendo a base de datos
        db.Actividad(nombre= nombre,
                     fechaInicio= fechaInicio,
                     fechaFin= fechaFin,
                     tipo= tipo,
                     imagen= imagen,
                     descripcion= descripcion,
                     evento= db.Evento.get(nombre=evento),
                     ambiente= db.Ambiente.get(nombre= ambiente),
                    )
        flash("Actividad agregada")
        return redirect(url_for('config.actividades'))
    return render_template("añadirActividad.html",form= form)
#CF-17-03
@bp.route('/modificarActividades/<id>', methods=['GET','POST'])
@login_required
def modificarActividad(id):
    form = FormValidarActividad()
    if request.method == 'POST':
        act = db.Actividad.get(id=int(id))
        if not act:
            flash("No existe esa actividad")
            return redirect(url_for('main.index'))
        
        act.nombre = form.nombre.data
        act.fechaInicio =  datetime.combine(form.fechaInicio.data, datetime.min.time())
        act.fechaFin = datetime.combine(form.fechaFin.data, datetime.min.time())
        act.tipo= form.tipo.data
        act.imagen= form.imagen.data
        act.descripcion = form.descripcion.data
        flash("Actividad modificada")
        return redirect(url_for('config.actividades'))
    return render_template("añadirActividad.html",form= form)
#---------------------------FIN ACTIVIDADES------------------------------------------------------------