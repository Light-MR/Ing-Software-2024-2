# Reyes Ramos Luz María
import random
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.sets = 0
        self.juegos = 0
        self.puntos = 0
        self.sacando = False

def marcador(jugador1, jugador2):
    print("\n----------------------")
    print("   Marcador:")
    print("Sets:")
    print(f"{jugador1.nombre} {jugador1.sets} - {jugador2.sets} {jugador2.nombre}")
    print("Juegos:")
    print(f"{jugador1.nombre} {jugador1.juegos} - {jugador2.juegos} {jugador2.nombre}")
    print("Puntuacion:")
    print(f"{jugador1.nombre} {jugador1.puntos} - {jugador2.puntos} {jugador2.nombre}")
    print("----------------------\n")


def anotar(opcion, jugador1, jugador2):
    anotador = jugador1 if opcion == 'a' else jugador2
    oponente = jugador2 if opcion == 'a' else jugador1
    print(f"\n{anotador.nombre} anotó!")
    if anotador.puntos == 0:
        anotador.puntos = 15
    elif anotador.puntos == 15:
        anotador.puntos = 30
    elif anotador.puntos == 30:
        anotador.puntos = 40
    elif anotador.puntos == 40:
        if oponente.puntos == "vent.":
            anotador.puntos, oponente.puntos = 40, 40
        elif oponente.puntos < 40:
            anotador.puntos = "juego"
        elif oponente.puntos == 40:
            anotador.puntos = "vent."
    elif anotador.puntos == "vent.":
        anotador.puntos = "juego"

def jugar(jugador1, jugador2):
    if (jugador1.juegos + jugador2.juegos) % 2 != 0:
        cambiar_cancha()
    print("\n ********* Iniciando el siguiente juego *************")
    
    # No es el primer juego y no es el primer set
    if jugador1.juegos + jugador2.juegos != 0 or jugador1.sets + jugador2.sets != 0:
        cambiar_saque(jugador1, jugador2)
    while jugador1.puntos != "juego" and jugador2.puntos != "juego":
        opcion= ' '
        while opcion != 'a' and opcion != 'b':
            marcador(jugador1, jugador2)
            try:
                opcion = input(f"Elige quien anota O_o:\na. {jugador1.nombre}\nb. {jugador2.nombre}\n")
                if opcion != 'a' and opcion != 'b':
                    print("Opción  no válida")
            except ValueError:
                print("Opción no válida")
        anotar(opcion, jugador1, jugador2)
    finalizar_juego(jugador1, jugador2)

def finalizar_juego(jugador1, jugador2):

    if jugador1.puntos == "juego":
        ganador = jugador1
    else: 
        ganador = jugador2
    
    ganador.juegos +=1
    print(f"\nGanador del juego: {ganador.nombre}")

    # Reiniciar 
    jugador1.puntos, jugador2.puntos = 0,0

        
def jugar_set(jugador1, jugador2):
    set_actual = jugador1.sets + jugador2.sets + 1
    while (jugador1.juegos < 6 and jugador2.juegos < 6) or abs(jugador1.juegos - jugador2.juegos) < 2:
        print(f"\nSet {set_actual} de {num_sets}")
        jugar(jugador1, jugador2)
    marcar_set(jugador1, jugador2)

def marcar_set(jugador1, jugador2):
    if jugador1.juegos > jugador2.juegos:
        ganador = jugador1
    else:
        ganador = jugador2
        
    ganador.sets += 1
    print(f"\n{ganador.nombre} marca este set!")
    if ganador.sets > num_sets//2:
        print("\nEl partido ha terminado porque un jugador ha ganado la mayoría de los sets (*.*)")
        return True

    # Reiniciar marcador
    jugador1.juegos = 0
    jugador2.juegos = 0



def cambiar_saque(jugador1, jugador2):
    #Se alternan los jugadores
    jugador1.sacando, jugador2.sacando = not jugador1.sacando, not jugador2.sacando
    print("\n-----> Cambio de saque")
    print("Saca", jugador1.nombre if jugador1.sacando else jugador2.nombre)

def cambiar_cancha():
    print("\n ---------------> Cambio de cancha <------------------------")


def simular_partido():
    global num_sets
    print("\n---------- Simulador de partido de tenis ٩(ˊᗜˋ*)و ----------------\n")
    jugador1_nombre = input("Ingresa el nombre del 1° jugador: ").strip()
    jugador2_nombre = input("Ingresa el nombre del 2° jugador: ").strip()

      # Solicitar al usuario el número de sets a jugar (siempre impar)
    while True:
        try:
            num_sets = int(input("Ingresa el número de sets a jugar (debe ser impar): "))
            if num_sets % 2 == 1:
                break
            else:
                print("El número de sets debe ser impar.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

    jugador1 = Jugador(jugador1_nombre)
    jugador2 = Jugador(jugador2_nombre)
    # Se elige aleatoriamente quien saca al inicio
    primero_sacar = random.choice([jugador1,jugador2])
    primero_sacar.sacando = True 
    print("\n Inicio de juego saca ->", primero_sacar.nombre)

    while True:
        if jugador1.sets > num_sets//2  or  jugador2.sets>num_sets//2:
            break
        print(f"\nInicia set numero:{jugador1.sets + jugador2.sets + 1}")
        jugar_set(jugador1, jugador2)

    print("\nFin de la partida")
    marcador(jugador1, jugador2)
    ganador = jugador1 if jugador1.sets > jugador2.sets else jugador2
    print(f"EL GANADOR DE ESTE PARTIDO ES: {ganador.nombre.upper()} ☜(ˆ▿ˆc)")

if __name__ == "__main__":
    simular_partido()