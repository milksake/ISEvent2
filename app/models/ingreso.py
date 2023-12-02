from app.extensions import db
from pony.orm import Required, Optional
from datetime import datetime

class Ingreso(db.Entity):
    monto = Required(int)
    descripcion = Required(str)
    fecha = Required(datetime)
    inscripcion = Optional("Inscripcion")
