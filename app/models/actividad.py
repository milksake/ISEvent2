from app.extensions import db
from pony.orm import Required, Set, db_session, Optional
from datetime import datetime

class Actividad(db.Entity):
    nombre = Required(str)
    fechaInicio= Required(datetime)
    fechaFin = Required(datetime)
    tipo= Required(str)
    imagen = Required(str)
    descripcion = Required(str)
    ambiente = Set('Ambiente') #1 actividad -> varios ambientes
    paquete = Set('Paquete')
    evento = Set('Evento') #1 actividad -> varios ambientes


#CF-17-04
@db_session
def createActividades():
    x = Actividad.get(nombre="Charla 1")
    if (x):
        x.delete()
    fechaIni = datetime(2012, 12, 12, 12, 00)
    fechaFin = datetime(2013, 1, 1, 1, 1)
    Actividad(nombre="Charla 1", 
              fechaInicio=fechaIni, 
              fechaFin= fechaFin, 
              tipo="Charla", 
              imagen="No Image",
              descripcion="Esta es una charla",
              ambiente = db.Ambiente.get(nombre="Green Hills"),
              evento= db.Evento.get(nombre="Evento Ejemplo"))
