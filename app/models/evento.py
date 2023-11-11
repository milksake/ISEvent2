from app.extensions import db
from pony.orm import Required, db_session
from datetime import datetime

class Evento(db.Entity):
    nombre = Required(str, unique=True)
    descripcion = Required(str)
    fechaInicio = Required(datetime)
    fechaFin = Required(datetime)
    imagen = Required(str)
    tipo = Required(str)

@db_session
def createEventos():
    x = Evento.get(nombre="Evento Ejemplo")
    if (x):
        x.delete()
    Evento(nombre="Evento Ejemplo", descripcion="Sample text", fechaInicio=datetime(2012, 12, 12, 12, 12), fechaFin=datetime(2013, 1, 1, 1, 1), imagen="Sample image", tipo="Conferencia")
