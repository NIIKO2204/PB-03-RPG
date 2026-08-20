
class Jugador:
    def __init__(self,nombre):

        self.nombre = nombre
        self.personaje = None

    def seleccionar_personaje(self,Personaje):
        self.personaje = self.personaje
        print(f"{self.nombre}" seleccio al pj f"{Personaje.nombre}")

    def mostrar_personaje(self):
        if self.personaje is not None:
            print(f"el jugador {self.nombre}"
                  f"utiliza a {self.personaje.nombre}")
        else:
            print("no se encontro")

    

