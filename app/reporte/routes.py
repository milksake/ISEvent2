from app.reporte import bp
from flask import render_template, request, flash, url_for, redirect, send_file, abort
from flask_login import current_user, login_required
from app.extensions import db
from pony.orm import group_concat, select
from datetime import datetime
from openpyxl import Workbook
from openpyxl.styles import Font

def generarExcel(titulos, datos, func):
    wb = Workbook()
    ws = wb.active
    ws.append(titulos)
    for d in datos:
        ws.append(func(d))
    ft = Font(bold=True)
    for row in ws[f"A1:{chr(ord('A')+len(titulos))}1"]:
        for cell in row:
            cell.font = ft
    
    wb.save("./app" + url_for('static', filename="archivos/reporte.xlsx"))

@bp.route('/inscritos/')
@bp.route('/inscritos/<id>', methods=['GET', 'POST'])
@login_required
def reporteInscritos(id = None):
    if not id:
        eves = None
        if current_user.rol == "admin":
            eves = db.Evento.select()
        elif current_user.rol == "encargado":
            eves = db.Evento.select(lambda e: e in current_user.comites.eventos)
        else:
            abort(403)
        return render_template("reporteInscritos.html", eventos=eves)
    eve = db.Evento.get(id=int(id))
    if not eve:
        flash("Ese evento no existe.")
        return redirect(url_for('main.index'))
    if current_user.rol != "admin" and not (current_user.rol == "encargado" and eve in current_user.comites.eventos):
        abort(403)
    ins = db.Inscripcion.select(lambda i: i.paquete.evento.id == id)
    rol = request.args.get('rol')
    if rol and rol != "None":
        ins = ins.filter(lambda i : i.paquete.rol == rol)
    actividades = request.args.get('actividades')
    if actividades and actividades != "None":
        ins = ins.filter(lambda i : group_concat((a.nombre for a in i.paquete.actividades), sep=', ') == actividades)
    fechaIni = request.args.get('fechaIni')
    if fechaIni and fechaIni != "":
        ins = ins.filter(lambda i : i.fecha >= datetime.strptime(fechaIni, '%Y-%m-%dT%H:%M'))
    fechaFin = request.args.get('fechaFin')
    if fechaFin and fechaFin != "":
        ins = ins.filter(lambda i : i.fecha <= datetime.strptime(fechaFin, '%Y-%m-%dT%H:%M'))
    if request.method == 'POST':
        f = lambda i : [i.cuenta.nombre, ', '.join([a.nombre for a in i.paquete.actividades]), i.paquete.rol, i.fecha]
        generarExcel(['Cuenta', 'Actividades', 'Rol', 'Fecha'], ins, f)
        return send_file("./"+ url_for('static', filename="archivos/reporte.xlsx"), download_name=f'reporte inscripciones {eve.nombre}.xlsx')
    return render_template("reporteInscritos.html", inscripciones=ins, evento=eve)

@bp.route('/asistencias/')
@bp.route('/asistencias/<id>', methods=['GET', 'POST'])
@login_required
def reporteAsistencias(id = None):
    if not id:
        eves = None
        if current_user.rol == "admin":
            eves = db.Evento.select()
        elif current_user.rol == "encargado":
            eves = db.Evento.select(lambda e: e in current_user.comites.eventos)
        else:
            abort(403)
        return render_template("reporteAsistencias.html", eventos=eves)
    eve = db.Evento.get(id=int(id))
    if not eve:
        flash("Ese evento no existe.")
        return redirect(url_for('main.index'))
    if current_user.rol != "admin" and not (current_user.rol == "encargado" and eve in current_user.comites.eventos):
        abort(403)
    query = select(i for i in db.Inscripcion if i.paquete.evento.id == int(id))
    acts = select(a for a in db.Actividad if a.evento.id == int(id))
    if request.method == 'POST':
        f = lambda i : [i.cuenta.nombre] + [a for a in select(a in i.asistencias for a in acts)]
        generarExcel(['Cuenta'] + [a.nombre for a in acts], query, f)
        return send_file("./"+ url_for('static', filename="archivos/reporte.xlsx"), download_name=f'reporte asistencias {eve.nombre}.xlsx')
    query = [[i, [a for a in select(a in i.asistencias for a in acts)]] for i in query]
    return render_template('reporteAsistencias.html', asistencias=query, evento=eve)

@bp.route('/materiales/')
@bp.route('/materiales/<id>', methods=['GET', 'POST'])
@login_required
def reporteMateriales(id = None):
    if not id:
        eves = None
        if current_user.rol == "admin":
            eves = db.Evento.select()
        elif current_user.rol == "encargado":
            eves = db.Evento.select(lambda e: e in current_user.comites.eventos)
        else:
            abort(403)
        return render_template("reporteMateriales.html", eventos=eves)
    eve = db.Evento.get(id=int(id))
    if not eve:
        flash("Ese evento no existe.")
        return redirect(url_for('main.index'))
    if current_user.rol != "admin" and not (current_user.rol == "encargado" and eve in current_user.comites.eventos):
        abort(403)
    query = select(m for m in db.Material if m.actividad.evento.id == int(id))
    if request.method == 'POST':
        f = lambda m : [m.nombre, m.cantidad, m.tipo, m.actividad.nombre]
        generarExcel(['Material', 'Cantidad', 'Tipo', 'Actividad'], query, f)
        return send_file("./"+ url_for('static', filename="archivos/reporte.xlsx"), download_name=f'reporte materiales {eve.nombre}.xlsx')
    return render_template('reporteMateriales.html', materiales=query, nombreEvento=eve.nombre)

@bp.route('/<tipo>/<id>', methods=['GET', 'POST'])
@login_required
def reporteCaja(tipo, id):
    eve = db.Evento.get(id=int(id))
    if not eve:
        flash("Ese evento no existe.")
        return redirect(url_for('main.index'))
    if current_user.rol != "admin" and not (current_user.rol == "encargado" and eve in current_user.comites.eventos):
        abort(403)
    if request.method == 'POST':
        query = None
        if tipo == 'ingresos':
            query = select(i for i in db.Ingreso if i.evento.id == int(id))
        elif tipo == 'egresos':
            query = select(i for i in db.Egreso if i.evento.id == int(id))
        else:
            flash("Reporte no válido")
            return redirect(url_for('main.index'))
        fechaIni = request.form['fechaIni']
        if fechaIni and fechaIni != "":
            query = query.filter(lambda i : i.fecha >= datetime.strptime(fechaIni, '%Y-%m-%dT%H:%M'))
        fechaFin = request.form['fechaFin']
        if fechaFin and fechaFin != "":
            query = query.filter(lambda i : i.fecha <= datetime.strptime(fechaFin, '%Y-%m-%dT%H:%M'))
        
        f = lambda m : [m.monto, m.descripcion, m.fecha]
        generarExcel(['Monto', 'Decripcion', 'Fecha'], query, f)
        return send_file("./"+ url_for('static', filename="archivos/reporte.xlsx"), download_name=f'reporte {tipo} {eve.nombre}.xlsx')
    return render_template('reporteCaja.html', tipo=tipo)