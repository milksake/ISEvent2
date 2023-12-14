from app.extensions import db
from pony.orm import Required, Optional, Set
from datetime import datetime

class Inscripcion(db.Entity):
    preinscripcion = Required(bool)
    documentoId = Required(str)
    nombres = Optional(str)
    apellidos = Optional(str)
    correo = Optional(str)
    fecha = Required(datetime)
    asistencia_validada = Required(bool, default=False)
    paquete = Required("Paquete")
    cuenta = Optional("Cuenta")
    ingreso = Optional("Ingreso")
    asistencias = Set("Actividad")
