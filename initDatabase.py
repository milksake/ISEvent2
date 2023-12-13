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
           rol="ninguno"),
    db.Cuenta(nombre="Maria",
              contrasena=generate_password_hash("maria"),
              correo="maria@mail.com",
              rol="ninguno")
    
    db.Cuenta(nombre="Luis",
              contrasena=generate_password_hash("luis"),
              correo="luis@mail.com",
              rol="ninguno")

    db.Cuenta(nombre="Ana",
              contrasena=generate_password_hash("ana"),
              correo="ana@mail.com",
              rol="ninguno")
    
    db.Cuenta(nombre="Juan",
              contrasena=generate_password_hash("juan"),
              correo="juan@mail.com",
              rol="ninguno")
    
    db.Cuenta(nombre="Elena",
              contrasena=generate_password_hash("elena"),
              correo="elena@mail.com",
              rol="ninguno")
    
    db.Cuenta(nombre="Carlos",
              contrasena=generate_password_hash("carlos"),
              correo="carlos@mail.com",
              rol="ninguno")
    
    db.Cuenta(nombre="Laura",
              contrasena=generate_password_hash("laura"),
              correo="laura@mail.com",
              rol="ninguno")
    
    db.Cuenta(nombre="Pablo",
              contrasena=generate_password_hash("pablo"),
              correo="pablo@mail.com",
              rol="ninguno")
    
    db.Cuenta(nombre="Isabel",
              contrasena=generate_password_hash("isabel"),
              correo="isabel@mail.com",
              rol="ninguno")
    
    db.Cuenta(nombre="Roberto",
              contrasena=generate_password_hash("roberto"),
              correo="roberto@mail.com",
              rol="ninguno")
    
@db_session
def createAmbientes():
    db.Ambiente(nombre="Sala de Auditorio",
                aforo=100,
                descripcion="El auditorio es un espacio íntimo y acogedor diseñado para albergar eventos con una capacidad moderada de audiencia. Con un diseño compacto pero funcional, dispone de filas de asientos dispuestas de manera que todos los espectadores disfruten de una excelente visibilidad. La disposición escalonada de las butacas asegura que cada asistente tenga una vista clara del escenario, creando un ambiente cercano que favorece la interacción y la conexión entre el público y los artistas o presentadores."
                )
    # nombre de la imagen "1.jpg"
    
    db.Ambiente(nombre="Sala de Laboratorio",
                aforo=30,
                descripcion="El salón de laboratorio cuenta con una disposición ordenada y funcional de 30 computadoras, creando un entorno propicio para actividades prácticas y experimentación en el ámbito informático. Las estaciones de trabajo están distribuidas de manera uniforme en filas, permitiendo un fácil acceso y movilidad para los usuarios."
                )
    # nombre de la imagen "2.jpg"
    
    db.Ambiente(nombre="Sala de Aula",
                aforo=30,
                descripcion="El aula con capacidad para 35 personas está diseñada para proporcionar un entorno educativo íntimo y colaborativo. Con un diseño eficiente, dispone de pupitres o mesas con sillas para acomodar a cada estudiante de manera cómoda y funcional. La disposición de los asientos está organizada para facilitar la interacción y la participación en discusiones en grupo."
                )
    # nombre de la imagen "3.jpg"
    
    db.Ambiente(nombre="Patio",
                aforo=100,
                descripcion="El patio es un espacio versátil y abierto diseñado para albergar una variedad de eventos y actividades. Con un diseño amplio y accesible, el patio ofrece flexibilidad para la creación de escenarios temporales y la realización de diversas presentaciones al aire libre."
                )
    # nombre de la imagen "4.jpg"
    
    # Agregar 6 ambientes más
    db.Ambiente(nombre="Sala de Conferencias",
                aforo=100,
                descripcion="La sala de conferencias está equipada con tecnología de punta y ofrece un entorno ideal para presentaciones y discusiones de alto nivel. El diseño del espacio permite una distribución cómoda de los asistentes, fomentando la participación y el intercambio de ideas."
                )
    # nombre de la imagen "5.jpg"
    
    db.Ambiente(nombre="Sala de Reuniones",
                aforo=20,
                descripcion="La sala de reuniones proporciona un entorno íntimo y privado para discusiones ejecutivas y reuniones de equipo. Con una disposición de mesa de conferencias y cómodas sillas, este ambiente favorece la toma de decisiones y la colaboración efectiva."
                )
    # nombre de la imagen "6.jpg"
    
    db.Ambiente(nombre="Sala de Exposiciones",
                aforo=40,
                descripcion="La sala de exposiciones ofrece un espacio amplio y bien iluminado para presentar obras de arte, proyectos o productos. Con paredes modulares y una disposición versátil, este ambiente es perfecto para exhibiciones creativas y eventos culturales."
                )
    # nombre de la imagen "7.jpg"
    
    db.Ambiente(nombre="Sala de Entrenamiento",
                aforo=40,
                descripcion="La sala de entrenamiento está equipada con recursos audiovisuales y mobiliario adaptable para facilitar sesiones de formación y desarrollo profesional. Con un diseño funcional, este ambiente permite a los participantes centrarse en el aprendizaje y la adquisición de habilidades."
                )
    # nombre de la imagen "8.jpg"
    
    db.Ambiente(nombre="Sala de Proyecciones",
                aforo=40,
                descripcion="La sala de proyecciones cuenta con un sistema de sonido e imagen de alta calidad, ofreciendo un espacio dedicado para la proyección de películas, presentaciones y eventos audiovisuales. Con asientos cómodos, este ambiente garantiza una experiencia inmersiva para los espectadores."
                )
    # nombre de la imagen "9.jpg"
    
    db.Ambiente(nombre="Sala de Estudio",
                aforo=15,
                descripcion="La sala de estudio proporciona un entorno tranquilo y enfocado para actividades académicas e investigación. Con mesas individuales y estanterías, este ambiente es ideal para estudiantes y profesionales que requieren un espacio para el estudio independiente."
                )
    # nombre de la imagen "10.jpg"

@db_session
def createEventos():
    fechaIni = datetime(2023, 12, 12, 12, 00)
    fechaFin = datetime(2024, 1, 1, 1, 1)
    fechaInsIni = datetime(2023, 12, 1, 18, 00)
    fechaInsFin = datetime(2023, 12, 30, 18, 00)
    
    ###########
    # EVENTOS #
    ###########

    comite_bienvenida = db.Comite(
        nombre="Comité de bienvenida",
        cuentas=[db.Cuenta.get(nombre="Pedro"), db.Cuenta.get(nombre="Antonio")])
    
    bienvenida_nuevos = db.Evento(
        nombre="Bienvenida a Estudiantes Nuevos",
        descripcion="La Bienvenida a Estudiantes Nuevos es una sesión informativa y acogedora diseñada para orientar a los recién llegados. Presenta servicios y recursos universitarios clave, creando un ambiente que facilita la transición y la integración de los estudiantes en la comunidad académica.",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        fechaInscripcionInicio=fechaInsIni,
        fechaInscripcionFin=fechaInsFin,
        tipo="Conferencia",
        comite=db.Comite.get(nombre="Comité de bienvenida")
    )
    #imagen: /static/imgs/eventos/1.jpg

    comite_clubes = db.Comite(
        nombre ="Comité de clubes",
        cuentas = []
    )

    feria_club = db.Evento(
        nombre="Feria de Clubes y Organizaciones Estudiantiles",
        descripcion="La Feria de Clubes ofrece a los estudiantes la oportunidad de explorar y unirse a diversas actividades extracurriculares. Los clubes presentan sus objetivos y actividades, fomentando la participación estudiantil y la construcción de conexiones sociales.",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        fechaInscripcionInicio=fechaInsIni,
        fechaInscripcionFin=fechaInsFin,
        tipo="Feria",
        comite=db.Comite.get(nombre="Comité de clubes")
    )
    #imagen: /static/imgs/eventos/2.jpg

    comite_social = db.Comite(
        nombre="Comité de Eventos Sociales",
        cuentas=[]
    )

    fiesta_bienvenida = db.Evento(
        nombre="Fiesta de Bienvenida al Semestre",
        descripcion="La Fiesta de Bienvenida al Semestre crea un ambiente relajado y social para que los estudiantes se conozcan. Proporciona una plataforma para la diversión y el establecimiento de conexiones informales, contribuyendo a la creación de relaciones en un entorno universitario más informal.",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        fechaInscripcionInicio=fechaInsIni,
        fechaInscripcionFin=fechaInsFin,
        tipo="Social",
        comite=comite_social
    )
    #imagen: /static/imgs/eventos/3.jpg

    comite_deportivo = db.Comite(
        nombre="Comité Deportivo",
        cuentas=[]
    )

    competencias_deportivas = db.Evento(
        nombre="Competencias Deportivas Interfacultades",
        descripcion="Las Competencias Deportivas fomentan la camaradería y la competencia saludable entre las facultades. Torneos y partidos deportivos promueven la participación estudiantil en actividades físicas, fortaleciendo los lazos entre los miembros de la comunidad académica.",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        fechaInscripcionInicio=fechaInsIni,
        fechaInscripcionFin=fechaInsFin,
        tipo="Deportivo",
        comite=comite_deportivo
    )
    #imagen: /static/imgs/eventos/4.jpg
    comite_sostenibilidad = db.Comite(
        nombre="Comité de Sostenibilidad",
        cuentas=[]
    )

    semana_sostenibilidad = db.Evento(
        nombre="Semana de la Sostenibilidad",
        descripcion="La Semana de la Sostenibilidad presenta talleres y charlas sobre prácticas ecoamigables. Ofrece actividades prácticas para elevar la conciencia ambiental entre los estudiantes, fomentando la responsabilidad social y la adopción de comportamientos sostenibles.",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        fechaInscripcionInicio=fechaInsIni,
        fechaInscripcionFin=fechaInsFin,
        tipo="Conferencia",
        comite=comite_sostenibilidad
    )
    #imagen: /static/imgs/eventos/5.jpg

    act_semana_sostenibilidad = db.Actividad(
        nombre = "Un mundo sostenible",
        fechaInicio = fechaIni,
        fechaFin = fechaFin,
        tipo="Conferencia",
        descripcion="Un Mundo Sostenible es una conferencia dedicada a la conciencia ambiental y prácticas sostenibles. Expertos en sostenibilidad comparten conocimientos sobre el impacto ambiental, la conservación de recursos y la importancia de adoptar estilos de vida ecoamigables. La actividad busca inspirar a los participantes a tomar medidas hacia un futuro más sostenible, promoviendo la responsabilidad individual y colectiva.",
        ambiente = db.Ambiente.get(nombre="Sala de Auditorio"),
        evento = semana_sostenibilidad
    )
    
    p1_semana_sostenibilidad = db.Paquete(
        precio=0.00,
        rol="Estudiante",
        evento=semana_sostenibilidad,
        actividades=[act_semana_sostenibilidad]
    )

    #############################

    comite_cultural = db.Comite(
        nombre="Comité Cultural",
        cuentas=[]
    )

    festival_cultural = db.Evento(
        nombre="Festival Cultural",
        descripcion="El Festival Cultural celebra la diversidad a través de exposiciones y presentaciones artísticas. Muestra la riqueza cultural de la comunidad universitaria con actuaciones musicales, danzas y exposiciones, promoviendo la apreciación intercultural y la inclusión.",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        fechaInscripcionInicio=fechaInsIni,
        fechaInscripcionFin=fechaInsFin,
        tipo="Cultural",
        comite=comite_cultural
    )
    #imagen: /static/imgs/eventos/6.jpg

    act_nuestra_propia_cultura = db.Actividad(
        nombre="Nuestra Propia Cultura",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        tipo="Cultural",
        descripcion="Nuestra Propia Cultura es una actividad que celebra la diversidad cultural dentro de la comunidad universitaria. Incluye exposiciones, presentaciones artísticas y muestras gastronómicas que destacan las distintas tradiciones presentes en el campus. Esta iniciativa promueve la apreciación intercultural, fomenta la inclusión y fortalece los lazos entre los miembros de la comunidad.",
        ambiente=db.Ambiente.get(nombre="Patio"),
        evento=db.Evento.get(nombre="Festival Cultural")
    )

    p1_nuestra_propia_cultura = db.Paquete(
        precio=8.00,  # Precio accesible para fomentar la participación
        rol="Estudiante",
        evento=db.Evento.get(nombre="Festival Cultural"),
        actividades=[act_nuestra_propia_cultura]
    )

    comite_empleabilidad = db.Comite(
        nombre="Comité de Empleabilidad",
        cuentas=[]
    )

    feria_empleo = db.Evento(
        nombre="Feria de Empleo y Prácticas",
        descripcion="La Feria de Empleo brinda a los estudiantes la oportunidad de explorar oportunidades laborales y de prácticas. Facilita la conexión entre estudiantes y empresas, fomentando la planificación de carreras y el desarrollo profesional desde el principio de la educación universitaria.",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        fechaInscripcionInicio=fechaInsIni,
        fechaInscripcionFin=fechaInsFin,
        tipo="Feria",
        comite=comite_empleabilidad
    )

    act_primer_empleo = db.Actividad(
        nombre="Primer Empleo",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        tipo="Feria",
        descripcion="La actividad Primer Empleo es una feria dedicada a proporcionar a los estudiantes la oportunidad de explorar opciones laborales y de prácticas. Empresas líderes en diversos sectores participan para presentar oportunidades de empleo, pasantías y programas de desarrollo profesional. Los estudiantes pueden interactuar con representantes de empresas, presentar sus currículums y establecer conexiones valiosas para su futura carrera.",
        ambiente=db.Ambiente.get(nombre="Sala de Laboratorio"),
        evento=db.Evento.get(nombre="Feria de Empleo y Prácticas")
    )

    p1_primer_empleo = db.Paquete(
        precio=0.00,  # Entrada gratuita para facilitar la participación
        rol="Estudiante",
        evento=db.Evento.get(nombre="Feria de Empleo y Prácticas"),
        actividades=[act_primer_empleo]
    )

    comite_talentos = db.Comite(
        nombre="Comité de Talentos",
        cuentas=[]
    )

    noche_talentos = db.Evento(
        nombre="Noche de Talentos",
        descripcion="La Noche de Talentos es una plataforma para que los estudiantes muestren sus habilidades artísticas. Desde música hasta comedia, esta velada destaca la diversidad de talentos dentro de la comunidad estudiantil, fomentando el espíritu creativo y la expresión personal.",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        fechaInscripcionInicio=fechaInsIni,
        fechaInscripcionFin=fechaInsFin,
        tipo="Cultural",
        comite=comite_talentos
    )

    act_presentacion_talentos = db.Actividad(
        nombre="Presentación de Talentos",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        tipo="Cultural",
        descripcion="La Presentación de Talentos es un evento destinado a destacar las habilidades artísticas y creativas de los estudiantes. Desde actuaciones musicales hasta exhibiciones de arte, esta actividad ofrece una plataforma para que los talentos emergentes muestren su destreza. Fomenta la expresión personal, la apreciación de las artes y el fortalecimiento de la comunidad a través del reconocimiento y la celebración del talento diverso presente en el campus.",
        ambiente=db.Ambiente.get(nombre="Sala de Auditorio"),
        evento=db.Evento.get(nombre="Noche de Talentos")
    )

    p1_presentacion_talentos = db.Paquete(
        precio=6.00,  # Precio accesible para fomentar la participación
        rol="Estudiante",
        evento=db.Evento.get(nombre="Noche de Talentos"),
        actividades=[act_presentacion_talentos]
    )

    #imagen: /static/imgs/eventos/8.jpg

    ###############
    # ACTIVIDADES #
    ###############

    act_conoce_companeros = db.Actividad(
        nombre = "Conoce a tus compañeros",
        fechaInicio = fechaIni,
        fechaFin = fechaFin,
        tipo = "Charla",
        descripcion = "Conoce a tus compañeros es una charla diseñada para fomentar la conexión y la camaradería entre los participantes. Durante la sesión, se brinda a cada miembro la oportunidad de compartir brevemente sus experiencias, intereses y objetivos. La charla busca crear un ambiente inclusivo, donde todos tengan la oportunidad de aprender más sobre sus colegas, promoviendo así la construcción de relaciones sólidas dentro del grupo. A través de este intercambio, se fortalece el sentido de comunidad y colaboración, creando una base positiva para futuras interacciones.",
        ambiente = db.Ambiente.get(nombre="Sala de Aula"),
        evento = bienvenida_nuevos
    )
    
    p1_conoce_companeros = db.Paquete(
        precio=0.00,
        rol="Estudiante",
        evento=fiesta_bienvenida,
        actividades=[act_conoce_companeros]
    )
    
    act_presentacion_clubes = db.Actividad(
    nombre="Presentación de Clubes",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        tipo="Presentación",
        descripcion="La Presentación de Clubes es un evento dedicado a destacar la diversidad de clubes y organizaciones estudiantiles en el campus. Cada club tiene la oportunidad de compartir sus objetivos, actividades y eventos planificados para el semestre. Esta actividad ofrece a los estudiantes la posibilidad de explorar opciones extracurriculares, unirse a clubes afines a sus intereses y conectarse con la vibrante vida estudiantil en la universidad.",
        ambiente=db.Ambiente.get(nombre="Sala de Auditorio"),
        evento=feria_club
    )

    p1_presentacion_clubes = db.Paquete(
        precio=0.00,  # Precio gratuito para fomentar la participación
        rol="Estudiante",
        evento=feria_club,
        actividades=[act_presentacion_clubes]
    )

    act_fiesta_bienvenida = db.Actividad(
        nombre="Baila con nosotros",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        tipo="Baile",
        descripcion="La Presentación de Clubes es un evento dedicado a destacar la diversidad de clubes y organizaciones estudiantiles en el campus. Cada club tiene la oportunidad de compartir sus objetivos, actividades y eventos planificados para el semestre. Esta actividad ofrece a los estudiantes la posibilidad de explorar opciones extracurriculares, unirse a clubes afines a sus intereses y conectarse con la vibrante vida estudiantil en la universidad.",
        ambiente=db.Ambiente.get(nombre="Patio"),
        evento=fiesta_bienvenida
    )

    p1_fiesta_bienvenida = db.Paquete(
        precio=0.00,
        rol="Estudiante",
        evento=fiesta_bienvenida,
        actividades=[act_fiesta_bienvenida]
    )

    act_manana_deportiva = db.Actividad(
        nombre="Mañana Deportiva",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        tipo="Deportivo",
        descripcion="La Mañana Deportiva es una jornada dedicada a la actividad física y la promoción de un estilo de vida saludable. Incluye una variedad de competiciones deportivas, juegos y actividades recreativas. Este evento fomenta la participación de la comunidad universitaria en actividades deportivas, fortaleciendo la camaradería y el bienestar general de los estudiantes.",
        ambiente=db.Ambiente.get(nombre="Patio"),
        evento=competencias_deportivas
    )

    p1_manana_deportiva = db.Paquete(
        precio=5.00,  # Precio accesible para incentivar la participación
        rol="Estudiante",
        evento=db.Evento.get(nombre="Competencias Deportivas Interfacultades"),
        actividades=[act_manana_deportiva]
    )

    
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