class Ambiente:
    def __init__(self, id, nombre, aforo, descripcion, imagen) -> None:
        self.idAmbiente = id
        self.nombre = nombre
        self.aforo = aforo
        self.descripcion = descripcion
        self.imagen = imagen

ambienteslist = [Ambiente("0", "Green Hills", "19", "Sample text", "Sample image")]

def get_ambiente_from_id(id):
    for ambiente in ambienteslist:
        if ambiente.id == id:
            return ambiente
    return None