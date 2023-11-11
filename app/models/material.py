from app.extensions import db
from pony.orm import Required

class Material(db.Entity):
    nombre = Required(str, unique=True)
    cantidad = Required(int)
    tipo = Required(str)
