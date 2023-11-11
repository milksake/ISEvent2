from app.extensions import db
from pony.orm import Required, db_session

class Ambiente(db.Entity):
    """
    def __init__(self, id, nombre, aforo, descripcion, imagen) -> None:
        self.idAmbiente = id
        self.nombre = nombre
        self.aforo = aforo
        self.descripcion = descripcion
        self.imagen = imagen
    """
    nombre = Required(str, unique=True)
    aforo = Required(int)
    descripcion = Required(str)
    imagen = Required(str)

#ambienteslist = [Ambiente("0", "Green Hills", "19", "Sample text", "Sample image")]
#CF-20-04
@db_session
def createAmbientes():
    x = Ambiente.get(nombre="Green Hills")
    if (x):
        x.delete()
    Ambiente(nombre="Green Hills", aforo=19, descripcion="Sample text", imagen="Sample image")

"""
def get_ambiente_from_id(id):
    for ambiente in ambienteslist:
        if ambiente.id == id:
            return ambiente
    return None
"""