from app.config import bp
from flask import render_template, request, flash, redirect, url_for, abort
from flask_login import login_required, current_user
from app.extensions import db
from datetime import datetime
from app.forms.FormValidarActividad import FormValidarActividad
from pony.orm import commit

############
# CF-03-01 #
############
@bp.route('/eventos')
@login_required
def eventos():
    even = None
    if current_user.rol == "admin":
        even = db.Evento.select()
    elif current_user.rol == "encargado":
        even = db.Evento.select(lambda e: e in current_user.comites.eventos)
    else:
        abort(403)
    return render_template("index.html", eventos=even, config=True)
# FIN ----------------------------------------------------------------------------------------------------

############
# CF-03-02 #
############
@bp.route('/añadirEvento', methods=['GET', 'POST'])
@login_required
def añadirEvento():
    if request.method == 'POST':
        file = request.files['imagen']
        if not file or file.filename == '' or file.filename.split('.')[-1].lower() not in ['jpg', 'png', 'jpeg']:
            flash('Seleccione una imagen válida')
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
        file.save("./app/" + url_for('static', filename=f"imgs/eventos/{newEve.id}.png"))
        flash("Evento agregado")
        return redirect(url_for('config.eventos'))
    comits = None
    if current_user.rol == "admin":
        comits = db.Comite.select()
    elif current_user.rol == "encargado":
        comits = current_user.comites
    else:
        abort(403)
    return render_template("añadirEvento.html", comites=comits)
# FIN ----------------------------------------------------------------------------------------------------


############
# CF-03-03 #
############
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
    comits = None
    if current_user.rol == "admin":
        comits = db.Comite.select()
    elif current_user.rol == "encargado":
        if ev not in current_user.comites.eventos:
            abort(403)
        comits = [cc for cc in current_user.comites if cc != ev.comite]
    else:
        abort(403)
    return render_template("añadirEvento.html", evento=ev, comites=comits)
#FIN

############
# CF-15-03 #
############
@bp.route('/paquetes')
@bp.route('/paquetes/<id>')
@login_required
def paquetes(id=None):
    if not id:
        evess = None
        if current_user.rol == "admin":
            evess = db.Evento.select()
        elif current_user.rol == "encargado":
            evess = db.Evento.select(lambda e: e in current_user.comites.eventos)
        else:
            abort(403)
        return render_template("paqueteUI.html", eventos=evess)
    eve = db.Evento.get(id=int(id))
    if (not eve):
        flash("Ese evento no existe")
        return redirect(url_for("main.index"))
    if current_user.rol != "admin" and not (current_user.rol == "encargado" and eve in current_user.comites.eventos):
        abort(403)
    return render_template("paqueteUI.html", evento=eve)

############
# CF-15-01 #
############
@bp.route('/añadirPaquete/<id>', methods=['GET', 'POST'])
@login_required
def añadirPaquete(id):
    eve = db.Evento.get(id=int(id))
    if not eve:
        flash("No existe ese evento")
        return redirect(url_for('main.index'))
    if current_user.rol != "admin" and not (current_user.rol == "encargado" and eve in current_user.comites.eventos):
        abort(403)
    if request.method == 'POST':
        acts_id = request.form.getlist('actividades')
        if len(acts_id) == 0:
            flash("Se tiene que elegir al menos una actividad")
            return redirect(url_for('main.index'))
        acts_id = [int(a) for a in acts_id]
        acts = db.Actividad.select(lambda a: a.id in acts_id)
        db.Paquete(
            precio = float(request.form['precio']),
            rol = request.form['rol'],
            evento = eve,
            actividades = acts,
        )
        flash("Paquete añadido")
        return redirect(url_for('config.paquetes', id=id))
    return render_template("añadirPaquete.html", evento=eve)
# FIN

############
# CF-15-02 #
############
@bp.route('/modificarPaquete/<id>', methods=['GET', 'POST'])
@login_required
def modificarPaquete(id):
    paq = db.Paquete.get(id=int(id))
    if current_user.rol != "admin" and not (current_user.rol == "encargado" and paq.evento in current_user.comites.eventos):
        abort(403)
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
        paq.precio = float(request.form['precio'])
        paq.rol = request.form['rol']
        paq.actividades = acts
        flash("Paquete modificado")
        return redirect(url_for('config.paquetes', id=paq.evento.id))
    return render_template("añadirPaquete.html", evento=paq.evento)
# FIN

############
# CF-20-01 #
############
@bp.route('/ambientes')
@login_required
def ambientes():
    if current_user.rol not in ['admin', 'encargado']:
        abort(403)
    amb = db.Ambiente.select(lambda a: request.args.get("query", default="") in a.nombre)
    return render_template("ambienteUI.html", ambientes=amb)
# FIN ----------------------------------------------------------------------------------------------------

############
# CF-20-02 #
############
@bp.route('/añadirAmbiente', methods=['GET', 'POST'])
@login_required
def añadirAmbiente():
    if current_user.rol not in ['admin', 'encargado']:
        abort(403)
    if request.method == 'POST':
        file = request.files['imagen']
        if not file or file.filename == '' or file.filename.split('.')[-1].lower() not in ['jpg', 'png', 'jpeg']:
            flash('Seleccione una imágen valida')
            return redirect(url_for('main.index'))
        nom = request.form['nombre']
        amb = db.Ambiente.get(nombre=nom)
        if amb:
            flash("Ese nombre de evento ya existe pruebe con otro")
            return redirect(url_for('main.index'))
        
        newAmb = db.Ambiente(nombre=request.form['nombre'],
                    aforo=request.form['aforo'],
                    descripcion=request.form['descripcion'])
        commit()
        file.save("./app/" + url_for('static', filename=f"imgs/ambientes/{newAmb.id}.png"))
        flash("Ambiente agregado")
        return redirect(url_for('config.ambientes'))
    return render_template("añadirAmbiente.html")
# FIN ----------------------------------------------------------------------------------------------------

############
# CF-20-03 #
############
@bp.route('/modificarAmbientes/<id>', methods=['GET','POST'])
@login_required
def modificarAmbiente(id):
    if current_user.rol not in ['admin', 'encargado']:
        abort(403)
    amb = db.Ambiente.get(id=int(id))
    if not amb:
        flash("No existe ese ambiente")
        return redirect(url_for('main.index'))
    if request.method == 'POST':
        nom = request.form['nombre']
        amb2 = db.Ambiente.get(nombre=nom)
        if amb2 and amb2.nombre != amb.nombre:
            flash("Ese nombre de evento ya existe")
            return redirect(url_for('main.index'))

        amb.nombre = nom
        amb.aforo = request.form['aforo']
        amb.descripcion = request.form['descripcion']

        file = request.files['imagen']
        if file and file.filename != '' and file.filename.split('.')[-1].lower() in ['jpg', 'png', 'jpeg']:
            file.save("./app/" + url_for('static', filename=f"imgs/ambientes/{amb.id}.png"))

        flash("Ambiente modificado")
        return redirect(url_for('config.ambientes'))
    return render_template("añadirAmbiente.html", ambiente=amb)
# FIN ----------------------------------------------------------------------------------------------------

############
# CF-18-01 #
############
@bp.route('/materiales')
@bp.route('/materiales/<id>')
@login_required
def materiales(id = None):
    if id:
        eve = db.Evento.get(id=int(id))
        if not eve:
            flash("Ese evento no existe")
            return redirect(url_for('main.index'))
        if current_user.rol != "admin" and not (current_user.rol == "encargado" and eve in current_user.comites.eventos):
            abort(403)
        mat = db.Material.select(lambda m : m.actividad.evento.id == int(id))
        return render_template("materialUI.html", materiales=mat, evento=eve)
    eves = None
    if current_user.rol == "admin":
        eves = db.Evento.select()
    elif current_user.rol == "encargado":
        eves = db.Evento.select(lambda e: e in current_user.comites.eventos)
    else:
        abort(403)
    return render_template('materialUI.html', eventos=eves)
# FIN ----------------------------------------------------------------------------------------------------

############
# CF-18-02 #
############
@bp.route('/añadirMaterial/<id>', methods=['GET', 'POST'])
@login_required
def añadirMaterial(id):
    eve = db.Evento.get(id=int(id))
    if not eve:
        flash("Ese evento no es válido")
        return redirect(url_for('main.index'))
    if current_user.rol != "admin" and not (current_user.rol == "encargado" and eve in current_user.comites.eventos):
            abort(403)
    if request.method == 'POST':
        act = db.Actividad.get(id=int(request.form['actividad']))
        if not act:
            flash("Actividad no válida")
            return redirect(url_for('main.index'))
        eg = db.Egreso(monto=float(request.form['costo']),
                       descripcion=f"Material: {request.form['cantidad']} {request.form['nombre']}",
                       fecha=datetime.now().replace(second=0, microsecond=0),
                       evento=eve)
        db.Material(nombre=request.form['nombre'],
                    cantidad=request.form['cantidad'],
                    tipo=request.form['tipo'],
                    egreso=eg,
                    actividad=act)
        flash("Material Creado")
        return redirect(url_for('config.materiales'))
    return render_template("añadirMaterial.html", actividades=eve.actividades)
# FIN ----------------------------------------------------------------------------------------------------

############
# CF-18-03 #
############
@bp.route('/modificarMaterial/<id>', methods=['GET', 'POST'])
@login_required
def modificarMaterial(id):
    mat = db.Material.get(id=int(id))
    if not mat:
        flash("Ese material no es válido")
        return redirect(url_for('main.index'))
    if current_user.rol != "admin" and not (current_user.rol == "encargado" and mat.actividad.evento in current_user.comites.eventos):
        abort(403)
    if request.method == 'POST':
        act = db.Actividad.get(id=int(request.form['actividad']))
        if not act:
            flash("Actividad no válida")
            return redirect(url_for('main.index'))
        mat.nombre = request.form['nombre']
        mat.cantidad = request.form['cantidad']
        mat.tipo = request.form['tipo']
        mat.actividad = act
        mat.egreso.monto=float(request.form['costo'])
        mat.egreso.descripcion=f"Material: {request.form['cantidad']} {request.form['nombre']}"
        mat.egreso.fecha=datetime.now().replace(second=0, microsecond=0)
        flash("Material Modificado")
        return redirect(url_for('config.materiales'))
    return render_template("añadirMaterial.html", actividades=mat.actividad.evento.actividades)
# FIN ----------------------------------------------------------------------------------------------------

############
# CF-17-01 #
############
@bp.route('/actividades')
@login_required
def actividades():
    act = None
    if current_user.rol == "admin":
        act = db.Actividad.select()
    elif current_user.rol == "encargado": 
        act = db.Actividad.select(lambda a : a.evento in current_user.comites.eventos)
    q = request.args.get("query", default="")
    act = act.filter(lambda a: q in a.nombre or q in a.evento.nombre or q in a.tipo)
    return render_template("actividadUI.html", actividades=act) #variable de template
# FIN ----------------------------------------------------------------------------------------------------

############
# CF-17-02 #
############
@bp.route('/añadirActividad', methods=['GET', 'POST'])
@login_required
def añadirActividad():
    form = FormValidarActividad()
    if request.method == 'POST' and form.validate():
        nombre = form.nombre.data
        fechaInicio= datetime.combine(form.fechaInicio.data, datetime.min.time())
        fechaFin= datetime.combine(form.fechaFin.data, datetime.min.time())
        tipo = form.tipo.data
        descripcion = form.descripcion.data
        evento= form.evento.data
        ambiente= form.ambiente.data
        evento = db.Evento.get(nombre= evento)
        if not evento or (current_user.rol != "admin" and not (current_user.rol == "encargado" and evento not in current_user.comites.eventos)):
            flash("Evento no válido")
            return redirect(url_for('config.actividades'))
        ambiente = db.Ambiente.get(nombre= ambiente)
        if not ambiente:
            flash("Ambiente no válido")
            return redirect(url_for('config.actividades'))
        
        #aniadiendo a base de datos
        db.Actividad(nombre= nombre,
                     fechaInicio= fechaInicio,
                     fechaFin= fechaFin,
                     tipo= tipo,
                     descripcion= descripcion,
                     evento= evento,
                     ambiente= ambiente
                    )
        flash("Actividad agregada")
        return redirect(url_for('config.actividades'))
    return render_template("añadirActividad.html",form= form)
# FIN

############
# CF-17-03 #
############
@bp.route('/modificarActividades/<id>', methods=['GET','POST'])
@login_required
def modificarActividad(id):
    act = db.Actividad.get(id=int(id))
    if not act:
        flash("No existe esa actividad")
        return redirect(url_for('main.index'))
    if current_user.rol != "admin" and not (current_user.rol == "encargado" and act.evento in current_user.comites.eventos):
            abort(403)
    form = FormValidarActividad()
    if request.method == 'POST':
        
        act.nombre = form.nombre.data
        act.fechaInicio = form.fechaInicio.data
        act.fechaFin = form.fechaFin.data
        act.tipo= form.tipo.data
        act.descripcion = form.descripcion.data

        print(act.evento.fechaInicio, type(act.evento.fechaInicio))
        print(form.fechaInicio.data, type(form.fechaInicio.data))
        if not act.evento.fechaInicio or form.fechaInicio.data < act.evento.fechaInicio:
            act.evento.fechaInicio = form.fechaInicio.data
        if not act.evento.fechaFin or act.evento.fechaFin < form.fechaFin.data:
            act.evento.fechaFin = form.fechaFin.data

        flash("Actividad modificada")
        return redirect(url_for('config.actividades'))
    return render_template("añadirActividad.html",form= form)
# FIN ----------------------------------------------------------------------------------------------------

############
# CF-17-03 #
############
@bp.route('/agregarExpositor', methods=['GET', 'POST'])
@login_required
def agregarExpositor():
    if current_user.rol not in ["admin", "encargado"]:
        abort(403)
    # Obtén el expositor (si existe) y las actividades
    expositor_id = request.args.get('expositor_id')
    expositor = db.Expositor.get(id=expositor_id) if expositor_id else None
    actividades = db.Actividad.select()

    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        descripcion = request.form['descripcion']
        actividades_ids = [int(id) for id in request.form.getlist('actividades')]  # Obtén las actividades seleccionadas
        exp = db.Expositor.get(nombre=nombre)
        
        if exp:
            db.Expositor.delete(exp)

        db.Expositor(
                nombre=nombre,
                correo=correo,
                descripcion=descripcion,
                actividades=[db.Actividad[id] for id in actividades_ids]
            )

        return redirect(url_for('config.actividades'))

    # Lógica para la parte GET del método, renderizar formulario, etc.
    return render_template('añadirExpositor.html', actividades=actividades, expositor=expositor)
