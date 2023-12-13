from app.extensions import db
from pony.orm import Required, Optional
from datetime import datetime

class Egreso(db.Entity):
    monto = Required(float)
    descripcion = Required(str)
    fecha = Required(datetime)
    material = Optional("Material")
    evento = Required("Evento")
