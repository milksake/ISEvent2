from flask import Blueprint

bp = Blueprint('gestion', __name__)

from app.gestion import routes