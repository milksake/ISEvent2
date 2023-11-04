from flask import Blueprint

bp = Blueprint('inscripcion', __name__)

from app.inscripcion import routes