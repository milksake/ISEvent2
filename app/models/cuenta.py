from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

class Cuenta(UserMixin):
    def __init__(self, id, nombre, contraseña, correo, rol, imagen, qr) -> None:
        self.id = id
        self.nombre = nombre
        self.contraseña = generate_password_hash(contraseña)
        self.correo = correo
        self.rol = rol
        self.imagen = imagen
        self.qr = qr

    def set_password(self, password):
        self.contraseña = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.contraseña, password)


users = [Cuenta("0", "admin", "devDynamo", "example@mail.com", "admin", None, None),
         Cuenta("1", "test", "qaz", "asdgaf@zdfadf", "ninguno", None, None)]


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
