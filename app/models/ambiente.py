from app.extensions import db
from pony.orm import Required, Set, db_session

class Ambiente(db.Entity):
    nombre = Required(str, unique=True)
    aforo = Required(int)
    descripcion = Required(str)
    imagen = Required(str)
    actividades = Set('Actividad')
    