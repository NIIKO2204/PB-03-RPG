

# clase Personaje
from inventario import Inventario

class Personaje:
    
    def __init__(self, nombre, nivel, vida):
        self.nombre = nombre
        self.nivel = nivel
        self.vida = vida
        self.inventario =  Inventario()

    def atacar(self):
        print( f"{self.nombre} realiza un ataque.")

    def recibir_danio(self,danio):
         self.vida -= danio

         if self.vida <= 0:
             self.vida = 0
             print(f"{self.vida} a llegado a cero murio.")

    def  usar_habilidad(self):
        print(f"{self.nombre} ha utilizado una habilidad")

    def mostrar_info(self):
        print("\n-------informacion------")
        print(f"nombre: {self.nombre}")
        print(f"nivel: {self.nivel}")
        print(f"vida: {self.vida}")