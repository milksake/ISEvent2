from app.asistencia import bp
from flask import render_template

@bp.route('/control')
def control():
    return render_template("index.html")

@bp.route('/entrega')
def entrega():
    return render_template("index.html")

