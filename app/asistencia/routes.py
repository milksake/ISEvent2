from app.asistencia import bp
from flask import render_template, request, Response

@bp.route('/control')
def control():
    return render_template("index.html")

@bp.route('/asistencia')
def asistencia():
    return render_template("asistenciaUI.html")

@bp.route('/tomarAsistencia', methods=['GET', 'POST'] )
def tomarAsistencia():
    if request.method == 'POST':
        print("Something else")
    return render_template("tomarAsistencia.html")

@bp.route('/entrega')
def entrega():
    return render_template("index.html")

