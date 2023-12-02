from app.extensions import db
from pony.orm import Required, Set

class Comite(db.Entity):
    nombre = Required(str, unique=True)
    eventos = Set("Evento")
    cuentas = Set("Cuenta")
