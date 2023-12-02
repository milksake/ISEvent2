from app.extensions import db
from pony.orm import Required, Set

class Expositor(db.Entity):
    nombre = Required(str, unique=True)
    correo = Required(str)
    descripcion = Required(str)
    actividades = Set("Actividad")
