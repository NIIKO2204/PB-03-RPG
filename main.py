from jugador import Jugador
from mago import Mago
from inventario import Inventario

#Método principal

def main():
    #crear jugador
    nuevo_jugador = Jugador("Niko")

    #crear pjs

    magician = Mago("Yuno",10,100,200)

    #asociar jugador con psj

    nuevo_jugador.seleccionar_personaje(magician)
    nuevo_jugador.mostrar_personaje()


    #ATAQUE DEL MAGO
    magician.atacar()

    #HABILIDAD DE MAGO
    magician.usar_habilidad()
    
if __name__ == "__main__":
    main()    

