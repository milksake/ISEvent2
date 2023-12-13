from app.extensions import db
from pony.orm import Required, Set, Optional
from datetime import datetime

class Evento(db.Entity):
    nombre = Required(str, unique=True)
    descripcion = Required(str)
    fechaInicio = Optional(datetime)
    fechaFin = Optional(datetime)
    fechaInscripcionInicio = Required(datetime)
    fechaInscripcionFin = Required(datetime)
    tipo = Required(str)
    paquetes = Set("Paquete")
    actividades = Set('Actividad')
    comite = Required("Comite")
    ingresos = Set("Ingreso")
    egresos = Set("Egreso")
