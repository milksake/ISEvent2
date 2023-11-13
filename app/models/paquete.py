from app.extensions import db
from pony.orm import Required, Set, composite_index

class Paquete(db.Entity):
    precio = Required(float)
    rol = Required(str)
    evento = Required('Evento')
    actividades = Set('Actividad')
    inscripciones = Set('Inscripcion')

