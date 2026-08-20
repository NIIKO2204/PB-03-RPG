class Objeto:
    def __init__(self,nombre,tipo):

        self.nombre = nombre
        self.tipo = tipo

    def mostrar_info(self):
        print(f"objeto: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        
