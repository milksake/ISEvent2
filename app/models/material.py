class Material:
    def __init__(self, id, nombre, cantidad, descripcion, tipo) -> None:
        self.idMaterial = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.tipo = tipo

materialesList = []