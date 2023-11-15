from app.extensions import db
from pony.orm import Required, db_session, Set
from datetime import datetime

class Evento(db.Entity):
    nombre = Required(str, unique=True)
    descripcion = Required(str)
    fechaInicio = Required(datetime)
    fechaFin = Required(datetime)
    imagen = Required(str)
    tipo = Required(str)
    paquetes = Set("Paquete")
    cuenta_eventos = Set("Cuenta")
    actividades = Set('Actividad')

@db_session
def createEventos():
    x = Evento.get(nombre="Evento Ejemplo")
    if (x is None): #correccion, borrabas el evento, pero no sus actividades asociadas
        fechaIni = datetime(2012, 12, 12, 12, 00)
        fechaFin = datetime(2013, 1, 1, 1, 1)
        e1 = Evento(
            nombre="Evento Ejemplo",
            descripcion="Sample text",
            fechaInicio=fechaIni,
            fechaFin=fechaFin,
            imagen="Sample image",
            tipo="Conferencia")
        act1 = db.Actividad(
            nombre = "Charla 1",
            fechaInicio = fechaIni,
            fechaFin = fechaFin,
            tipo = "Charla",
            imagen = "No image",
            descripcion = "Esta es una charla",
            ambiente = db.Ambiente.get(nombre="Green Hills"),
            evento = e1)
        p1 = db.Paquete(
            precio = 10.50,
            rol = "estudiante",
            evento = e1,
            actividades = [act1])
        p2 = db.Paquete(precio = 12.50,
            rol = "profesional",
            evento = e1,
            actividades = [act1])
        act1.paquetes = [p1, p2]
        e1.paquetes = [p1, p2]
        e1.actividades= [act1]

