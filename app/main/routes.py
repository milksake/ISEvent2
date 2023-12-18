from app.main import bp
from flask import render_template
from app.extensions import db

#########################
# VER TODOS LOS EVENTOS #
#########################
@bp.route('/')
def index():
    even = db.Evento.select(lambda e : True)
    return render_template("index.html", eventos=even, config=False)
