from flask_login import UserMixin
from werkzeug.security import check_password_hash
from app.extensions import db
from pony.orm import Required, Set, Optional, db_session

class Cuenta(db.Entity, UserMixin):
    nombre = Required(str, unique=True)
    contrasena = Required(str)
    correo = Required(str, unique=True)
    rol = Required(str)
    inscripciones = Set("Inscripcion")
    comites = Set("Comite")

    def check_password(self, password):
        return check_password_hash(self.contrasena, password)
