from config import Config
from pony.orm import db_session
from werkzeug.security import generate_password_hash
from datetime import datetime
from app.extensions import db

@db_session
def createUsers():
    db.Cuenta(nombre="admin",
           contrasena=generate_password_hash("devDynamo"),
           correo="admin@mail.com",
           rol="admin")
    db.Cuenta(nombre="Pedro",
           contrasena=generate_password_hash("pedro"),
           correo="pedro@mail.com",
           rol="ninguno")
    db.Cuenta(nombre="Antonio",
           contrasena=generate_password_hash("antonio"),
           correo="antonio@mail.com",
           rol="ninguno")
    db.Cuenta(nombre="Federico",
           contrasena=generate_password_hash("federico"),
           correo="federico@mail.com",
           rol="ninguno")

@db_session
def createAmbientes():
    db.Ambiente(nombre="Auditorio1",
                aforo=100,
                descripcion="El auditorio es un espacio íntimo y acogedor diseñado para albergar eventos con una capacidad moderada de audiencia. Con un diseño compacto pero funcional, dispone de filas de asientos dispuestas de manera que todos los espectadores disfruten de una excelente visibilidad. La disposición escalonada de las butacas asegura que cada asistente tenga una vista clara del escenario, creando un ambiente cercano que favorece la interacción y la conexión entre el público y los artistas o presentadores.",
                )
    #nombre de la imagen "1.jpg"

    db.Ambiente(nombre="Laboratorio1",
                aforo=30,
                descripcion="El salón de laboratorio cuenta con una disposición ordenada y funcional de 30 computadoras, creando un entorno propicio para actividades prácticas y experimentación en el ámbito informático. Las estaciones de trabajo están distribuidas de manera uniforme en filas, permitiendo un fácil acceso y movilidad para los usuarios."
                )
    #nombre de la imagen "2.jpg"
    db.Ambiente(nombre="Aula1",
                aforo=30,
                descripcion="El aula con capacidad para 35 personas está diseñada para proporcionar un entorno educativo íntimo y colaborativo. Con un diseño eficiente, dispone de pupitres o mesas con sillas para acomodar a cada estudiante de manera cómoda y funcional. La disposición de los asientos está organizada para facilitar la interacción y la participación en discusiones en grupo."
                )
    #nombre de la imagen "3.jpg"
    db.Ambiente(nombre="Patio1",
                aforo=30,
                descripcion="El patio es un espacio versátil y abierto diseñado para albergar una variedad de eventos y actividades. Con un diseño amplio y accesible, el patio ofrece flexibilidad para la creación de escenarios temporales y la realización de diversas presentaciones al aire libre. "
                )
    #nombre de la imagen "4.jpg"
    

@db_session
def createEventos():
    fechaIni = datetime(2023, 12, 12, 12, 00)
    fechaFin = datetime(2024, 1, 1, 1, 1)
    fechaInsIni = datetime(2023, 12, 1, 18, 00)
    fechaInsFin = datetime(2023, 12, 10, 18, 00)
    
    com1 = db.Comite(
        nombre="Comité de bienvenida",
        cuentas=[db.Cuenta.get(nombre="Pedro"), db.Cuenta.get(nombre="Antonio")])
    e1 = db.Evento(
        nombre="Evento de introducción",
        descripcion="El evento de introducción es una ocasión especial diseñada para dar la bienvenida a participantes, ya sean nuevos estudiantes, empleados o miembros de una comunidad. Este encuentro proporciona una plataforma para presentar de manera amigable el entorno, los objetivos y las personas clave relacionadas con la institución o el grupo en cuestión.",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        fechaInscripcionInicio=fechaInsIni,
        fechaInscripcionFin=fechaInsFin,
        tipo="Conferencia",
        comite=com1)
    #imagen: /static/imgs/eventos/1.jpg
    act1 = db.Actividad(
        nombre = "Conoce a tus compañeros",
        fechaInicio = fechaIni,
        fechaFin = fechaFin,
        tipo = "Charla",
        descripcion = "Conoce a tus compañeros es una charla diseñada para fomentar la conexión y la camaradería entre los participantes. Durante la sesión, se brinda a cada miembro la oportunidad de compartir brevemente sus experiencias, intereses y objetivos. La charla busca crear un ambiente inclusivo, donde todos tengan la oportunidad de aprender más sobre sus colegas, promoviendo así la construcción de relaciones sólidas dentro del grupo. A través de este intercambio, se fortalece el sentido de comunidad y colaboración, creando una base positiva para futuras interacciones.",
        ambiente = db.Ambiente.get(nombre="Aula1"),
        evento = e1)
    p1 = db.Paquete(
        precio = 10.50,
        rol = "Invitado",
        evento = e1,
        actividades = [act1])
    p2 = db.Paquete(precio = 12.50,
        rol = "Estudiante",
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