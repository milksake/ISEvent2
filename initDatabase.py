from config import Config
from pony.orm import db_session
from werkzeug.security import generate_password_hash
from datetime import datetime
from app.extensions import db
import random
import qrcode

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
    # Lista sin repetidos
    ambientes = [
        "Sala de Aula",
        "Sala de Auditorio",
        "Aulas Creativas",
        "Patio",
        "Área de Juegos",
        "Salón Temático",
        "Área de Cine",
        "Campo Deportivo",
        "Pista de Atletismo",
        "Cancha de Vóley Playa",
        "Salón de Debates",
        "Área de Servicio",
        "Salón de Juegos",
        "Sala de Talleres",
        "Sala de Conferencias",
        "Reserva Natural",
        "Escenario Principal",
        "Galería de Arte",
        "Sala de Danza",
        "Sala de Laboratorio",
        "Área de Networking",
    ]

    descripciones = [
        "Una sala de aula es un espacio destinado al aprendizaje y la enseñanza. Suele estar equipada con mesas, sillas y pizarras. Aquí, los estudiantes y profesores se reúnen para explorar y compartir conocimientos.",
        "Una sala de auditorio es un lugar diseñado para conferencias, presentaciones y eventos. Suele contar con asientos dispuestos en filas, un escenario y equipo de audiovisual para brindar una experiencia educativa o de entretenimiento.",
        "Las aulas creativas son espacios inspiradores donde la imaginación y la innovación florecen. Equipadas con recursos variados, fomentan el pensamiento creativo y el desarrollo de habilidades artísticas y técnicas.",
        "El patio es un espacio al aire libre destinado al recreo y la relajación. Puede incluir áreas verdes, bancos y juegos, ofreciendo un entorno agradable para actividades sociales y físicas.",
        "El área de juegos es un lugar diseñado para la diversión y el entretenimiento. Equipada con estructuras para trepar, columpios y juegos interactivos, promueve el ejercicio y la interacción social entre niños y adultos.",
        "Un salón temático es un espacio decorado de manera única para reflejar un tema específico. Puede utilizarse para eventos, fiestas o actividades relacionadas con la temática elegida.",
        "El área de cine es un lugar equipado con proyectores y asientos cómodos para la proyección de películas y eventos audiovisuales. Proporciona una experiencia cinematográfica inmersiva.",
        "Un campo deportivo es un espacio al aire libre dedicado a actividades físicas y deportivas. Puede incluir canchas de fútbol, baloncesto, tenis u otros deportes, ofreciendo oportunidades para la competición y el ejercicio.",
        "Una pista de atletismo es un recorrido circular diseñado para carreras y eventos deportivos. Suele contar con carriles específicos para diferentes disciplinas atléticas como la carrera, el salto y el lanzamiento.",
        "Una cancha de vóley playa es un área de arena destinada a juegos de vóley playa. Ofrece un entorno informal y relajado para disfrutar de este deporte en un ambiente playero.",
        "Un salón de debates es un espacio donde se llevan a cabo discusiones formales sobre temas específicos. Puede utilizarse para eventos académicos, políticos o comunitarios que fomenten la expresión de ideas y la argumentación.",
        "Un área de servicio es un espacio destinado a brindar comodidades y recursos a las personas. Puede incluir áreas de descanso, máquinas expendedoras y servicios básicos para satisfacer necesidades específicas.",
        "Un salón de juegos es un lugar equipado con mesas de juegos como billar, ping pong y juegos de mesa. Ofrece un ambiente recreativo para socializar y disfrutar de diversas actividades lúdicas.",
        "Una sala de talleres es un espacio diseñado para actividades prácticas y creativas. Puede utilizarse para clases, talleres y actividades que fomenten el aprendizaje práctico y la experimentación.",
        "Una sala de conferencias es un espacio formal para presentaciones, charlas y eventos. Suele contar con asientos cómodos, equipo audiovisual y un escenario, proporcionando un entorno propicio para el intercambio de conocimientos.",
        "Una reserva natural es un área protegida que conserva la biodiversidad y los ecosistemas naturales. Ofrece oportunidades para la observación de la naturaleza y la educación ambiental.",
        "El escenario principal es un área destinada a presentaciones y actuaciones destacadas. Puede encontrarse en teatros, salas de conciertos o eventos, proporcionando un lugar central para espectáculos y actuaciones en vivo.",
        "Una galería de arte es un espacio dedicado a la exhibición y apreciación de obras de arte. Proporciona un entorno cultural para la contemplación de diversas expresiones artísticas.",
        "Una sala de danza es un espacio diseñado para prácticas y presentaciones de danza. Suele contar con espejos, barras y un suelo adecuado para facilitar la expresión artística a través del movimiento.",
        "Una sala de laboratorio es un espacio equipado con herramientas y equipos especializados para la realización de experimentos y análisis. Se utiliza en entornos educativos y científicos para investigaciones y descubrimientos.",
        "Un área de networking es un espacio diseñado para facilitar la interacción y la conexión entre individuos. Puede incluir zonas de encuentro, eventos sociales y recursos para fomentar relaciones profesionales y personales.",
    ]


    # Capacidad genérica para los ambientes
    capacidad = 50  # Puedes ajustar este valor según tus necesidades

    # Crear objetos db.Ambiente para cada elemento de la lista
    for ambiente_nombre, descripcion in zip(ambientes, descripciones):
        db.Ambiente(nombre=ambiente_nombre,
        aforo=capacidad,
        descripcion=descripcion
        )

@db_session
def createEventos():
    fechaIni = datetime(2023, 12, 12, 12, 00)
    fechaFin = datetime(2024, 1, 1, 1, 1)
    fechaInsIni = datetime(2023, 12, 1, 18, 00)
    fechaInsFin = datetime(2023, 12, 30, 18, 00)
    
    #########################
    # EVENTOS Y ACTIVIDADES #
    #########################

    # Evento 1

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

    act_conoce_companeros = db.Actividad(
        nombre = "Conoce a tus compañeros",
        fechaInicio = fechaIni,
        fechaFin = fechaFin,
        tipo = "Charla",
        descripcion = "Conoce a tus compañeros es una charla diseñada para fomentar la conexión y la camaradería entre los participantes. Durante la sesión, se brinda a cada miembro la oportunidad de compartir brevemente sus experiencias, intereses y objetivos. La charla busca crear un ambiente inclusivo, donde todos tengan la oportunidad de aprender más sobre sus colegas, promoviendo así la construcción de relaciones sólidas dentro del grupo. A través de este intercambio, se fortalece el sentido de comunidad y colaboración, creando una base positiva para futuras interacciones.",
        ambiente = db.Ambiente.get(nombre="Sala de Aula"),
        evento = bienvenida_nuevos
    )

    act_conoce_la_plataforma = db.Actividad(
        nombre = "Conoce la plataforma virtual",
        fechaInicio = fechaIni,
        fechaFin = fechaFin,
        tipo = "Charla",
        descripcion = "Conoce el entorno en el que estarás trabajando constantemente desde incluso antes de tu primera clase. En esta charla se busca dar una introduccion a los estudiantes de las características de la plataforma virtual en la que podrán hacer seguimiento de su progreso académico o de sus notas. Con la ayuda de profesores que ya están familiarizados, los estudiantes podrán usar de la mejor manera posible la plataforma.",
        ambiente = db.Ambiente.get(nombre="Sala de Aula"),
        evento = bienvenida_nuevos
    )
    
    act_conoce_local = db.Actividad(
        nombre = "Conoce el entorno en el que estarás estudiando",
        fechaInicio = fechaIni,
        fechaFin = fechaFin,
        tipo = "Charla",
        descripcion = "Conoce el local donde estarás pasando los próximos 5 años de tu vida, con esta introducción podrás ubicarte y guiar a otras personas alrededor de la universidad sin dificultades.",
        ambiente = db.Ambiente.get(nombre="Patio"),
        evento = bienvenida_nuevos
    )

    act_manual_supervivencia = db.Actividad(
        nombre = "Manual de supervivencia universitaria",
        fechaInicio = fechaIni,
        fechaFin = fechaFin,
        tipo = "Charla",
        descripcion = "Conoce los mejores consejos dados por otros estudiantes universitarios que ya pasaron por lo que pronto te pasará a ti. Aprende como es que se pueden prevenir problemas y lidiar con situaciones cotidianas en este nuevo ámbito que puede ser muy diferente a lo que estabas acostumbrado, haz más facil tu adaptación al nuevo mundo y prepárate para tu primer día de clases. Presta atención a los más experimentados y anota sus sugerencias, puede que en un futuro tu mismo puedas ayudar a otros estudiantes que comienzan aquí mejorando esos consejos que recibiste.",
        ambiente = db.Ambiente.get(nombre="Sala de Aula"),
        evento = bienvenida_nuevos
    )
    
    p1_bienvenida_estudiantes = db.Paquete(
        precio=0.00,
        rol="Estudiante",
        evento=bienvenida_nuevos,
        actividades=[act_conoce_companeros, act_conoce_la_plataforma, act_manual_supervivencia, act_conoce_local]
    )

    ############################################

    comite_clubes = db.Comite(
        nombre="Comité de clubes",
        cuentas=[]
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

    act_presentacion_clubes = db.Actividad(
        nombre="Presentación de Clubes",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        tipo="Presentación",
        descripcion="La Presentación de Clubes es un evento dedicado a destacar la diversidad de clubes y organizaciones estudiantiles en el campus. Cada club tiene la oportunidad de compartir sus objetivos, actividades y eventos planificados para el semestre. Esta actividad ofrece a los estudiantes la posibilidad de explorar opciones extracurriculares, unirse a clubes afines a sus intereses y conectarse con la vibrante vida estudiantil en la universidad.",
        ambiente=db.Ambiente.get(nombre="Sala de Auditorio"),
        evento=feria_club
    )

    act_forma_club = db.Actividad(
        nombre="¿Cómo puedo hacer mi propio club?",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        tipo="Presentación",
        descripcion="Quizás ninguno de los clubs te llama la atención lo suficiente, entonces ¿Que puedes hacer?. Muy fácil, puedes formar tu propio club pero debes cumplir con una serie de requisitos, para ello te daremos una serie de recomendaciones.",
        ambiente=db.Ambiente.get(nombre="Sala de Auditorio"),
        evento=feria_club
    )

    act_talleres_creativos = db.Actividad(
        nombre="Talleres Creativos",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        tipo="Taller",
        descripcion="Participa en talleres creativos organizados por diferentes clubes para explorar y desarrollar tus habilidades artísticas y creativas.",
        ambiente=db.Ambiente.get(nombre="Aulas Creativas"),
        evento=feria_club
    )

    act_debate_club = db.Actividad(
        nombre="Debate Club",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        tipo="Debate",
        descripcion="El Debate Club ofrece la oportunidad de participar en debates estimulantes sobre una variedad de temas. Únete para mejorar tus habilidades de argumentación y expresión oral.",
        ambiente=db.Ambiente.get(nombre="Salón de Debates"),
        evento=feria_club
    )

    act_servicio_comunitario = db.Actividad(
        nombre="Servicio Comunitario",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        tipo="Voluntariado",
        descripcion="Colabora con clubes involucrados en actividades de servicio comunitario. Descubre cómo puedes contribuir positivamente a la comunidad mientras te unes a un club.",
        ambiente=db.Ambiente.get(nombre="Área de Servicio"),
        evento=feria_club
    )

    act_torneo_esport = db.Actividad(
        nombre="Torneo Esport",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        tipo="Torneo",
        descripcion="Participa en torneos esport organizados por clubes especializados en deportes electrónicos. Demuestra tus habilidades en juegos competitivos y forma parte de la comunidad esport de la universidad.",
        ambiente=db.Ambiente.get(nombre="Salón de Juegos"),
        evento=feria_club
    )

    # Paquete actualizado
    p1_feria_club = db.Paquete(
        precio=10.00,
        rol="Estudiante",
        evento=feria_club,
        actividades=[act_presentacion_clubes, act_forma_club, act_talleres_creativos, act_debate_club, act_servicio_comunitario, act_torneo_esport]
    )

    #########################

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

    # Nuevas actividades para el Comité de Eventos Sociales
    act_karaoke_noche = db.Actividad(
        nombre="Noche de Karaoke",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        tipo="Entretenimiento",
        descripcion="Participa en una noche llena de música y diversión con una sesión de karaoke. Conoce a otros estudiantes mientras disfrutas de tu canción favorita.",
        ambiente=db.Ambiente.get(nombre="Salón de Juegos"),
        evento=fiesta_bienvenida
    )

    act_juegos_sociales = db.Actividad(
        nombre="Juegos Sociales",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        tipo="Juegos",
        descripcion="Únete a divertidos juegos sociales diseñados para romper el hielo y fomentar la interacción entre los estudiantes. ¡Haz nuevos amigos mientras te diviertes!",
        ambiente=db.Ambiente.get(nombre="Área de Juegos"),
        evento=fiesta_bienvenida
    )

    act_noche_tematica = db.Actividad(
        nombre="Noche Temática",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        tipo="Social",
        descripcion="Disfruta de una noche temática llena de sorpresas. Pueden haber disfraces, decoraciones y actividades relacionadas con el tema de la noche. ¡Vive una experiencia única con tus compañeros!",
        ambiente=db.Ambiente.get(nombre="Salón Temático"),
        evento=fiesta_bienvenida
    )

    act_cine_al_aire_libre = db.Actividad(
        nombre="Cine al Aire Libre",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        tipo="Cine",
        descripcion="Relájate bajo las estrellas mientras disfrutas de una película proyectada al aire libre. Tráete una manta y algo de snacks para una noche de cine bajo el cielo.",
        ambiente=db.Ambiente.get(nombre="Área de Cine"),
        evento=fiesta_bienvenida
    )

    # Paquete actualizado para la Fiesta de Bienvenida al Semestre
    p1_fiesta_bienvenida = db.Paquete(
        precio=10.00,
        rol="Estudiante",
        evento=fiesta_bienvenida,
        actividades=[act_karaoke_noche, act_juegos_sociales, act_noche_tematica, act_cine_al_aire_libre]
    )

    # Nuevo paquete para la Fiesta de Bienvenida al Semestre
    p2_fiesta_bienvenida = db.Paquete(
        precio=5.00,  # Se establece un precio para este paquete
        rol="Invitado",
        evento=fiesta_bienvenida,
        actividades=[act_karaoke_noche, act_juegos_sociales, act_noche_tematica, act_cine_al_aire_libre]
    )

    #########################

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

    act_torneo_futbol = db.Actividad(
        nombre="Torneo de Fútbol",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        tipo="Torneo",
        descripcion="Participa en el emocionante torneo de fútbol interfacultades. Forma un equipo con tus compañeros de facultad y compite por la victoria.",
        ambiente=db.Ambiente.get(nombre="Campo Deportivo"),
        evento=competencias_deportivas
    )

    act_carrera_atletica = db.Actividad(
        nombre="Carrera Atlética",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        tipo="Competencia",
        descripcion="Demuestra tu resistencia en la carrera atlética interfacultades. Corre junto a estudiantes de otras facultades y vive la emoción de la competición.",
        ambiente=db.Ambiente.get(nombre="Pista de Atletismo"),
        evento=competencias_deportivas
    )

    act_voley_playa = db.Actividad(
        nombre="Torneo de Vóley Playa",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        tipo="Torneo",
        descripcion="Forma parte del torneo de vóley playa interfacultades. Disfruta de un día de sol, arena y competencia amistosa.",
        ambiente=db.Ambiente.get(nombre="Cancha de Vóley Playa"),
        evento=competencias_deportivas
    )

    act_gimnasia_artistica = db.Actividad(
        nombre="Exhibición de Gimnasia Artística",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        tipo="Exhibición",
        descripcion="Disfruta de una impresionante exhibición de gimnasia artística. Los estudiantes mostrarán sus habilidades y destrezas en una presentación emocionante.",
        ambiente=db.Ambiente.get(nombre="Sala de Danza"),
        evento=competencias_deportivas
    )

    # Paquete 1 para Competencias Deportivas
    p1_competencias_deportivas = db.Paquete(
        precio=15.00,
        rol="Estudiante",
        evento=competencias_deportivas,
        actividades=[act_torneo_futbol, act_carrera_atletica, act_voley_playa, act_gimnasia_artistica]
    )

    # Paquete 2 para Competencias Deportivas
    p2_competencias_deportivas = db.Paquete(
        precio=5.00,
        rol="Invitado",
        evento=competencias_deportivas,
        actividades=[act_torneo_futbol, act_carrera_atletica, act_voley_playa, act_gimnasia_artistica]
    )

    ##############################

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

    act_taller_reciclaje = db.Actividad(
        nombre="Taller de Reciclaje Creativo",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        tipo="Taller",
        descripcion="Participa en un taller práctico de reciclaje creativo. Aprende a reutilizar materiales y a crear objetos útiles y decorativos a partir de materiales reciclados.",
        ambiente=db.Ambiente.get(nombre="Sala de Talleres"),
        evento=semana_sostenibilidad
    )

    act_charla_consumo_responsable = db.Actividad(
        nombre="Charla sobre Consumo Responsable",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        tipo="Charla",
        descripcion="Descubre la importancia del consumo responsable. La charla abordará temas como la elección de productos sostenibles, la reducción del desperdicio y la toma de decisiones informadas para un estilo de vida más sostenible.",
        ambiente=db.Ambiente.get(nombre="Sala de Conferencias"),
        evento=semana_sostenibilidad
    )

    act_excursion_naturaleza = db.Actividad(
        nombre="Excursión a la Naturaleza",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        tipo="Excursión",
        descripcion="Únete a una emocionante excursión a la naturaleza. Explora un entorno natural, aprende sobre la biodiversidad y conecta con la belleza del medio ambiente.",
        ambiente=db.Ambiente.get(nombre="Reserva Natural"),
        evento=semana_sostenibilidad
    )

    # Paquete 1 para la Semana de la Sostenibilidad
    p1_semana_sostenibilidad = db.Paquete(
        precio=20.00,
        rol="Estudiante",
        evento=semana_sostenibilidad,
        actividades=[act_semana_sostenibilidad, act_taller_reciclaje, act_charla_consumo_responsable, act_excursion_naturaleza]
    )

    # Paquete 2 para la Semana de la Sostenibilidad
    p2_semana_sostenibilidad = db.Paquete(
        precio=5.00,
        rol="Estudiante",
        evento=semana_sostenibilidad,
        actividades=[act_semana_sostenibilidad, act_taller_reciclaje, act_charla_consumo_responsable, act_excursion_naturaleza]
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

    act_presentacion_musical = db.Actividad(
    nombre="Presentación Musical",
    fechaInicio=fechaIni,
    fechaFin=fechaFin,
    tipo="Presentación",
    descripcion="Disfruta de talentosas presentaciones musicales que representan diferentes géneros y tradiciones. Celebra la diversidad sonora de nuestra comunidad universitaria.",
    ambiente=db.Ambiente.get(nombre="Escenario Principal"),
    evento=festival_cultural
    )

    act_exposicion_artistica = db.Actividad(
        nombre="Exposición Artística",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        tipo="Exposición",
        descripcion="Explora la creatividad y el arte en nuestra Exposición Artística. Estudiantes presentarán sus obras, mostrando la diversidad de expresiones artísticas en la comunidad universitaria.",
        ambiente=db.Ambiente.get(nombre="Galería de Arte"),
        evento=festival_cultural
    )

    act_taller_danza_tradicional = db.Actividad(
        nombre="Taller de Danza Tradicional",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        tipo="Taller",
        descripcion="Participa en un taller de danza tradicional donde podrás aprender movimientos y coreografías representativas de diversas culturas. Una experiencia divertida y educativa.",
        ambiente=db.Ambiente.get(nombre="Sala de Danza"),
        evento=festival_cultural
    )

    # Paquete 1 para el Festival Cultural
    p1_festival_cultural = db.Paquete(
        precio=8.00,
        rol="Estudiante",
        evento=festival_cultural,
        actividades=[act_nuestra_propia_cultura, act_exposicion_artistica, act_presentacion_musical, act_taller_danza_tradicional]
    )

    # Paquete 2 para el Festival Cultural
    p2_festival_cultural = db.Paquete(
        precio=12.00,
        rol="Estudiante",
        evento=festival_cultural,
        actividades=[act_nuestra_propia_cultura, act_exposicion_artistica, act_presentacion_musical, act_taller_danza_tradicional]
    )

    ##################################################

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

    act_taller_habilidades_profesionales = db.Actividad(
        nombre="Taller de Habilidades Profesionales",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        tipo="Taller",
        descripcion="Participa en un taller dedicado al desarrollo de habilidades profesionales clave, como la redacción de currículums, técnicas de entrevista y la construcción de una marca personal. Mejora tus habilidades para destacar en el mercado laboral.",
        ambiente=db.Ambiente.get(nombre="Sala de Conferencias"),
        evento=feria_empleo
    )

    act_sesion_networking = db.Actividad(
        nombre="Sesión de Networking",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        tipo="Networking",
        descripcion="Únete a una sesión de networking donde podrás interactuar directamente con representantes de empresas. Amplía tu red profesional y descubre oportunidades de empleo y prácticas.",
        ambiente=db.Ambiente.get(nombre="Área de Networking"),
        evento=feria_empleo
    )

    # Paquete 1 para la Feria de Empleo y Prácticas
    p1_feria_empleo = db.Paquete(
        precio=0.00,
        rol="Estudiante",
        evento=feria_empleo,
        actividades=[act_primer_empleo, act_taller_habilidades_profesionales, act_sesion_networking]
    )

    # Paquete 2 para la Feria de Empleo y Prácticas
    p2_feria_empleo = db.Paquete(
        precio=5.00,
        rol="Estudiante",
        evento=feria_empleo,
        actividades=[act_primer_empleo, act_taller_habilidades_profesionales, act_sesion_networking]
    )

    ###################################################

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

    act_exhibicion_arte = db.Actividad(
        nombre="Exhibición de Arte",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        tipo="Exhibición",
        descripcion="Participa en una exhibición de arte donde los estudiantes pueden mostrar sus creaciones artísticas, desde pinturas hasta esculturas. Celebra la diversidad de expresiones artísticas presentes en la comunidad universitaria.",
        ambiente=db.Ambiente.get(nombre="Galería de Arte"),
        evento=noche_talentos
    )

    act_comedia_stand_up = db.Actividad(
        nombre="Noche de Comedia Stand-Up",
        fechaInicio=fechaIni,
        fechaFin=fechaFin,
        tipo="Comedia",
        descripcion="Disfruta de una noche llena de risas con actuaciones de comedia stand-up. Estudiantes talentosos presentarán sus mejores rutinas humorísticas, proporcionando entretenimiento y diversión a la comunidad universitaria.",
        ambiente=db.Ambiente.get(nombre="Sala de Auditorio"),
        evento=noche_talentos
    )

    # Paquete 1 para la Noche de Talentos
    p1_noche_talentos = db.Paquete(
        precio=6.00,
        rol="Estudiante",
        evento=noche_talentos,
        actividades=[act_presentacion_talentos, act_exhibicion_arte, act_comedia_stand_up]
    )

    # Paquete 2 para la Noche de Talentos
    p2_noche_talentos = db.Paquete(
        precio=10.00,  # Precio ajustado para ofrecer una experiencia más completa
        rol="Estudiante",
        evento=noche_talentos,
        actividades=[act_presentacion_talentos, act_exhibicion_arte, act_comedia_stand_up]
    )

# INICIO CREACION DE PAQUETES E INSCRIPCIONES
@db_session
def createRandomIngreso():
    year= 2023
    month= random.randint(1,12)
    day= random.randrange(1,28)
    hour= random.randint(0,23)
    minute= random.randint(0,59)
    paquete= db.Paquete.get(id= random.randint(1,14))
    nuevoIngreso= db.Ingreso(
        monto= paquete.precio,
        descripcion= "Nueva inscripción.",
        fecha= datetime(year,month,day,hour,minute),
        evento= db.Evento.get(id= random.randint(1,8)),
    )
    db.commit()
    nuevaInscripcion= db.Inscripcion(
        preinscripcion= 0,
        documentoId= str(random.randrange(70000000, 80000000)),
        fecha= datetime(year,month,day,hour,minute),
        asistencia_validada= 0,
        paquete= paquete,
        cuenta= db.Cuenta.get(id= random.randint(1,14)),
        ingreso= nuevoIngreso,
        asistencias= [],
        precio= paquete.precio,
    )
    db.commit()
    nuevoIngreso.inscripcion= nuevaInscripcion

    primary_key= nuevoIngreso.inscripcion.id
    # Generar el código QR de los inscritos
    nombre_qr= nuevoIngreso.inscripcion.cuenta.nombre
    paquete_qr= ''
    for act in paquete.actividades:
        paquete_qr+= act.nombre+','
    qr = qrcode.make(str(primary_key))
    qr_path = f"app/static/qr/{nombre_qr+'-'+paquete_qr}.png"
    qr.save(qr_path)

@db_session
def createIngresos():
    for i in range(15):
        createRandomIngreso()
    
# FIN CREACION DE PAQUETES E INSCRIPCIONES

# INICIO CREACION DE EGRESOS Y MATERIALES
@db_session
def createRandomEgreso(nombre,tipo):
    year= 2023
    month= random.randint(1,12)
    day= random.randrange(1,28)
    hour= random.randint(0,23)
    minute= random.randint(0,59)

    nuevoEgreso= db.Egreso(
        monto= random.randint(10,100),
        descripcion= 'Compra de nuevo material.',
        fecha= datetime(year,month,day,hour,minute),
        evento= db.Evento.get(id= random.randint(1,8)),
    )
    db.commit()
    nuevoMaterial= db.Material(
        nombre = nombre,
        cantidad = random.randint(1,20),
        tipo = tipo,
        actividad = random.randint(1,32),
        egreso = db.Egreso.get(id= nuevoEgreso.id),
    )
    db.commit()
    nuevoEgreso.material= nuevoMaterial
    nuevoEgreso.descripcion= 'Compra de nuevo material: '+nuevoMaterial.nombre


@db_session
def createEgresos():
    nombres= ["Acero", "Aluminio", "Cobre", "Vidrio", "Plástico", "Madera", "Piedra", "Papel", "Cartón", "Goma", "Hierro", "Latón", "Nylon", "Tela", "Caucho", "Cemento", "Titanio", "Fibra de vidrio", "Porcelana", "Platino",
            "Tungsteno", "Cromo", "Silicio", "Bambú", "Cerámica", "Granito", "Mármol", "Zinc", "Plomo", "Polietileno", "Polipropileno", "Oro", "Plata", "Bronce", "Níquel", "Resina", "Fibra de carbono", "Cuero", "Corcho"]

    tipos = ["Escritorio", "Arte", "Oficina", "Manualidades", "Juguetes", "Limpieza", "Construcción", "Electrónica", "Cocina",
         "Herramientas", "Pintura", "Material escolar", "Papelaría", "Adhesivos", "Corte", "Escuela", "Artículos de escritura", "Decoración", "Iluminación",
         "Costura", "Bricolaje", "Hardware", "Baterías", "Lámparas"]

    for i in range(len(nombres)):
        tipo= tipos[random.randint(0, len(tipos) - 1)]
        createRandomEgreso(nombres[i],tipo)
    
# FIN CRECION DE EGRESOS Y MATERIALES
        
# INICIO CREACION DE COMITES
@db_session
def createRandomComite(comite):
    db.Comite(
        nombre= comite,
        eventos= [db.Evento.get(id= random.randint(1,8))],
        cuentas= [db.Cuenta.get(id= random.randint(1,14)),
                  db.Cuenta.get(id= random.randint(1,14))],
    )

@db_session
def createComites():
    comites= [
    "Comité de Organización", "Comité de Programa","Comité de Patrocinio", "Comité de Marketing",
    "Comité de Logística", "Comité de Comunicación","Comité de Entretenimiento", "Comité de Evaluación", 
    "Comité de Tecnología","Comité de Redes Sociales","Comité de Estudio de Hábitos Alimenticios de Mascotas",
    "Comité de Investigación de Sonidos Subacuáticos","Comité de Evaluación de Efectos del Color en el Entorno Laboral",
    "Comité de Optimización de Rutinas Matutinas","Comité de Preservación del Arte Urbano Efímero",
    "Comité de Análisis de Tendencias en Sombreros","Comité de Exploración de Tecnologías de Limpieza Sostenible",
    "Comité de Estudio de Relaciones entre Café y Creatividad","Comité de Investigación de Usos Alternativos para Globos de Helio",
    "Comité de Observación de Patrones de Sueño en Estudiantes de Ciencias de la Computación",
]
    for i in range(len(comites)):
        createRandomComite(comites[i])

# FIN CREACION DE COMITES
        
#INICIO CREACION EXPOSITORES
@db_session
def createRandomExpositor(expositor,descripcion):
    db.Expositor(
        nombre= expositor,
        correo= expositor+'_prueba@gmail.com',
        descripcion= descripcion,
        actividades= [db.Actividad.get(id= random.randint(1,32))],
    )

@db_session
def createExpositores():
    descripciones = [
    "Experta en inteligencia artificial y líder en innovación tecnológica.",
    "Reconocido autor y conferencista internacional en liderazgo y motivación.",
    "Pionero en la industria de la sostenibilidad y energías renovables.",
    "Emprendedora exitosa en el ámbito de la tecnología financiera (fintech).",
    "Especialista en marketing digital y estrategias de contenido en redes sociales.",
    ]
    expositores = [
    "Ana Martínez", "Carlos Rodríguez", "Elena García", "Francisco López", "Isabel Pérez",
    "Javier Hernández", "Laura Sánchez", "Miguel Fernández", "Natalia González", "Óscar Ramírez",
    "Patricia Díaz", "Roberto Ruiz", "Sara Torres", "Tomás Jiménez", "Verónica Moreno",
    "Alejandro Vargas", "Beatriz Castro", "César Navarro", "Diana Herrera", "Emilio Mendoza",
    "Fabiola Reyes", "Gustavo Aguilar", "Hilda Ortega", "Iván Silva", "Julia Núñez",
    "Luis Medina", "Marina Ríos", "Nacho Herrera", "Olga García",
    ]
    for i in range(len(expositores)):
        createRandomExpositor(expositores[i],descripciones[random.randint(0,4)])

#FIN CREACION EXPOSITORES
        
@db_session
def createPosers():
    db.Expositor(
        nombre="Javier Ibaerrechea",
        correo="javier@mail.com",
        descripcion="Javier es un estudiante de cuarto año de la carrera Derecho, uno de los alumnos más destacados con un promedio que lo hace destacar y un punto de vista diferente.",
        actividades=[db.Actividad.get(nombre="Conoce a tus compañeros"), db.Actividad.get(nombre="Conoce la plataforma virtual")]
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
createPosers()
createIngresos()
createEgresos()
createComites()
createExpositores()