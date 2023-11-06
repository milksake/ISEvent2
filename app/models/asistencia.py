class Asistencia:
    def __init__(self, idAsistencia) -> None:
        self.idAsistencia = idAsistencia
        self.cumplido = 0

asistenciaList = [Asistencia("111")]

def get_ambiente_from_id(id):
    for asistencia in asistenciaList:
        if asistencia.id == id:
            return asistencia
    return None