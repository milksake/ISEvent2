from pony.orm import Database

db = Database()

from app.models.cuenta import Cuenta
from app.models.ambiente import Ambiente
from app.models.inscripcion import Inscripcion
from app.models.actividad import Actividad 
from app.models.paquete import Paquete
from app.models.evento import Evento
from app.models.material import Material
from app.models.comite import Comite
from app.models.egreso import Egreso
from app.models.expositor import Expositor
from app.models.ingreso import Ingreso