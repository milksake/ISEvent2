from flask import Blueprint

bp = Blueprint('asistencia', __name__)

from app.asistencia import routes