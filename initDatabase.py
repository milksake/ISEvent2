from config import Config
from pony.orm import db_session
from werkzeug.security import generate_password_hash
from datetime import datetime
from app.extensions import db

@db_session
def createUsers():
    db.Cuenta(nombre="admin",
           contrasena=generate_password_hash("devDynamo"),
           correo="example@mail.com",
           rol="admin")
    db.Cuenta(nombre="test",
           contrasena=generate_password_hash("qazoo"),
           correo="asdgaf@zdfadf",
           rol="ninguno")
    db.Cuenta(nombre="test2",
           contrasena=generate_password_hash("qwerty"),
           correo="asdgafggg@zdfadgggf",
           rol="ninguno")
    db.Cuenta(nombre="test3",
           contrasena=generate_password_hash("123456"),
           correo="affffsdgaf@zdfaffffdf",
           rol="ninguno")

@db_session
def createAmbientes():
    db.Ambiente(nombre="Green Hills", aforo=19, descripcion="Sample text")

@db_session
def createEventos():
    fechaIni = datetime(2023, 12, 12, 12, 00)
    fechaFin = datetime(2024, 1, 1, 1, 1)
    fechaInsIni = datetime(2023, 12, 1, 18, 00)
    fechaInsFin = datetime(2023, 12, 10, 18, 00)
    
    com1 = db.Comite(
        nombre="Comite 1",
        cuentas=[db.Cuenta.get(nombre="test"), db.Cuenta.get(nombre="test3")])
    e1 = db.Evento(
        nombre="Evento Ejemplo",
        descripcion="Sample text",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        fechaInscripcionInicio=fechaInsIni,
        fechaInscripcionFin=fechaInsFin,
        tipo="Conferencia",
        comite=com1)
    act1 = db.Actividad(
        nombre = "Charla 1",
        fechaInicio = fechaIni,
        fechaFin = fechaFin,
        tipo = "Charla",
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
    e1.paquetes = [p1, p2]
    
config = Config
config.PONY['create_db'] = True
config.PONY['filename'] = 'app/' + config.PONY['filename']

# Pony Database
db.bind(**config.PONY)
db.generate_mapping(create_tables=True)

# Initialize DB
createUsers()
createAmbientes()
createEventos()