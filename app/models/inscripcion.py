from app.extensions import db
from pony.orm import Required

class Inscripcion(db.Entity):
    documentoId = Required(str)
    paquete = Required("Paquete")
    cuenta = Required("Cuenta")

