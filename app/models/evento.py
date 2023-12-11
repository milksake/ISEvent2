from app.extensions import db
from pony.orm import Required, db_session, Set, Optional
from datetime import datetime

class Evento(db.Entity):
    nombre = Required(str, unique=True)
    descripcion = Required(str)
    fechaInicio = Required(datetime)
    fechaFin = Required(datetime)
    fechaInscripcion = Required(datetime)
    imagen = Required(str)
    tipo = Required(str)
    paquetes = Set("Paquete")
    actividades = Set('Actividad')
    comite = Optional("Comite")
