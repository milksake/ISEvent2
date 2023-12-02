from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from app.extensions import db
from pony.orm import Required, Set, Optional, db_session

class Cuenta(db.Entity, UserMixin):
    nombre = Required(str, unique=True)
    contrasena = Required(str)
    correo = Required(str, unique=True)
    rol = Required(str)
    imagen = Optional(str)
    inscripciones = Set("Inscripcion")
    comites = Set("Comite")

    def check_password(self, password):
        return check_password_hash(self.contrasena, password)

@db_session
def createUsers():
    x = Cuenta.get(nombre="admin")
    if (x):
        x.delete()
    Cuenta(nombre="admin",
           contrasena=generate_password_hash("devDynamo"),
           correo="example@mail.com",
           rol="admin")
    x = Cuenta.get(nombre="test")
    if (x):
        x.delete()
    Cuenta(nombre="test",
           contrasena=generate_password_hash("qazoo"),
           correo="asdgaf@zdfadf",
           rol="ninguno")

"""
def obtenerCuenta(query):
    all = []
    for user in users:
        if query in user.nombre:
            all.append(user)
    return all

def get_user(username):
    for user in users:
        if user.nombre == username:
            return user
    return None


def get_user_from_id(id):
    for user in users:
        if user.id == id:
            return user
    return None


def get_user_from_email(email):
    for user in users:
        if user.correo == email:
            return user
    return None
"""