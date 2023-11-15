from app.extensions import db
from pony.orm import Required, Set, db_session

class Ambiente(db.Entity):
    nombre = Required(str, unique=True)
    aforo = Required(int)
    descripcion = Required(str)
    imagen = Required(str)
    actividades = Set('Actividad')
    

#ambienteslist = [Ambiente("0", "Green Hills", "19", "Sample text", "Sample image")]
#CF-20-04
@db_session
def createAmbientes():
    x = Ambiente.get(nombre="Green Hills")
    if (x):
        x.delete()
    Ambiente(nombre="Green Hills", aforo=19, descripcion="Sample text", imagen="Sample image")
