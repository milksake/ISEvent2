from extensions import db
from pony.orm.core import Required, db_session

class Actividad(db.Entity):
    nombre = Required(str)
    fecha_inicio = Required(str)
    fecha_fin = Required(str)
    tipo_actividad = Required(str)
    imagen_actividad = Required(str)
    descripcion = Required(str)

# Esto es importante para que PonyORM genere el mapeo
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
