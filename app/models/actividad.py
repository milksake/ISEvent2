from app.extensions import db
from pony.orm import Required, Set, db_session, Optional
from datetime import datetime

class Actividad(db.Entity):
    nombre = Required(str)
    fechaInicio = Required(datetime)
    fechaFin = Required(datetime)
    tipo = Required(str)
    imagen = Required(str)
    descripcion = Required(str)
    ambiente = Required('Ambiente')
    evento = Required('Evento')
    paquetes = Set('Paquete')
    expositores = Set("Expositor")
