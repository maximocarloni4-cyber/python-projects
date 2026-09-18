victorias_bj=0
jugador_bj=""
partidas_jugadas = 0
def blackjack():
    import random
    import os

    indice_mazo = 0
    casilleros_jugador = 0
    casilleros_crupier = 0
    puntos_jugador = 0
    puntos_crupier = 0
    valor_carta_crupier = 0
    valor_carta_jugador = 0
    cartas_jugador = [' '] * 8    #8 por el máximo de cartas que se puede tener en una sola mano
    cartas_crupier = [' '] * 8
    casillero = 0
    valores = ["2", "3","4","5","6","7","8","9","10","J","Q","K","A"]
    palos = ["♠", "♥", "♦", "♣"]
    mazo = [' '] * 52
    ases_jugador = 0
    ases_crupier = 0
    opcion_bj = 0
    jugar_bj = "si"
    
    def introduccion_bj():
        global jugador_bj
        print("\033[91m╔════════════════╗")
        print("║  BLACKJACK 🃏  ║")
        print("╚════════════════╝\033[0m")
        print("\033[33m📌 REGLAS:\033[0m")
        print("\033[32m- El objetivo es sumar 21 puntos o acercarse lo máximo posible.")
        print("- Podés pedir cartas o plantarte cuando quieras.")
        print("- Si superás los 21 puntos, perdés automáticamente.")
        print("- La banca pide cartas hasta alcanzar 17 puntos.")
        print("- Gana quien obtenga más puntos sin superar los 21.\033[0m\n")
        jugador_bj=str(input("Ingrese su nombre: "))
        input("Presione 'Enter' para continuar...")

    def mazo_bj():
        nonlocal mazo
        casillero = 0
        for i in range (4):
            for j in range (13):
                mazo[casillero]=valores[j],palos[i]
                casillero+= 1
        random.shuffle(mazo)

    def reparto_inicial_bj():
        nonlocal cartas_jugador
        nonlocal cartas_crupier
        nonlocal casilleros_jugador 
        nonlocal casilleros_crupier
        nonlocal indice_mazo
        nonlocal mazo
    
        for k in range (2):
            cartas_jugador[casilleros_jugador]=mazo[indice_mazo]
            casilleros_jugador += 1
            indice_mazo += 1
            cartas_crupier[casilleros_crupier]=mazo[indice_mazo]
            casilleros_crupier += 1
            indice_mazo += 1

    def puntos_jugador_bj():
        nonlocal puntos_jugador
        nonlocal ases_jugador
        nonlocal cartas_jugador
        nonlocal casilleros_jugador
        puntos_jugador = 0
        ases_jugador = 0
    
        for l in range(casilleros_jugador):
            valor_carta_jugador = cartas_jugador[l][0]
            match valor_carta_jugador:
                case "2": puntos_jugador += 2
                case "3": puntos_jugador += 3
                case "4": puntos_jugador += 4
                case "5": puntos_jugador += 5
                case "6": puntos_jugador += 6
                case "7": puntos_jugador += 7
                case "8": puntos_jugador += 8
                case "9": puntos_jugador += 9
                case "10": puntos_jugador += 10
                case "J": puntos_jugador += 10
                case "Q": puntos_jugador += 10
                case "K": puntos_jugador += 10
                case "A": puntos_jugador += 11; ases_jugador += 1
    
        while (puntos_jugador > 21 and ases_jugador > 0):
            puntos_jugador = puntos_jugador - 10
            ases_jugador -= 1

    def puntos_crupier_bj():
        nonlocal puntos_crupier
        nonlocal ases_crupier
        nonlocal casilleros_crupier
        nonlocal cartas_crupier
        puntos_crupier = 0
        ases_crupier = 0
    
        for p in range(casilleros_crupier):
            valor_carta_crupier = cartas_crupier[p][0]
            match valor_carta_crupier:
                case "2": puntos_crupier += 2
                case "3": puntos_crupier += 3
                case "4": puntos_crupier += 4
                case "5": puntos_crupier += 5
                case "6": puntos_crupier += 6
                case "7": puntos_crupier += 7
                case "8": puntos_crupier += 8
                case "9": puntos_crupier += 9
                case "10": puntos_crupier += 10
                case "J": puntos_crupier += 10
                case "Q": puntos_crupier += 10
                case "K": puntos_crupier += 10
                case "A": puntos_crupier += 11; ases_crupier += 1


        while (puntos_crupier>21 and ases_crupier>0):
            puntos_crupier = puntos_crupier - 10
            ases_crupier -= 1
    
    def mostrar_puntos_jugador_bj():
        print("\033[31mJugador\033[0m")
        for x in range (casilleros_jugador):
            print("┌─────┐", end=" ")
        print()
        
        for x in range(casilleros_jugador):
            valor_jug_bj = cartas_jugador[x][0]
            print(f"│{valor_jug_bj:<2}   │", end=" ")
        print()
        
        for x in range(casilleros_jugador):
            palo_jug_bj = cartas_jugador[x][1]
            if palo_jug_bj == "♥" or palo_jug_bj == "♦":
                palo_jug_bj = f"\033[91m{palo_jug_bj}\033[0m"
            else:
                palo_jug_bj = f"\033[30m{palo_jug_bj}\033[0m"
            print(f"│  {palo_jug_bj}  │", end=" ")
        print()
        
        for x in range(casilleros_jugador):
            valor_jug_bj = cartas_jugador[x][0]
            print(f"│   {valor_jug_bj:>2}│", end=" ")
        print()
        
        for x in range (casilleros_jugador):
            print("└─────┘", end=" ")
        print()
        
        print("\033[31m",puntos_jugador,"Puntos\033[0m")

    def mostrar_puntos_crupier_bj():
        print("\033[32mCrupier\033[0m")
        for y in range (casilleros_crupier):
            print("┌─────┐", end=" ")
        print()
        
        for y in range(casilleros_crupier):
            valor_cru_bj = cartas_crupier[y][0]
            print(f"│{valor_cru_bj:<2}   │", end=" ")
        print()
        
        for y in range(casilleros_crupier):
            palo_cru_bj = cartas_crupier[y][1]
            if palo_cru_bj == "♥" or palo_cru_bj == "♦":
                palo_cru_bj = f"\033[91m{palo_cru_bj}\033[0m"
            else:
                palo_cru_bj = f"\033[30m{palo_cru_bj}\033[0m"
            print(f"│  {palo_cru_bj}  │", end=" ")
        print()
        
        for y in range(casilleros_crupier):
            valor_cru_bj = cartas_crupier[y][0]
            print(f"│   {valor_cru_bj:>2}│", end=" ")
        print()
        
        for y in range (casilleros_crupier):
            print("└─────┘", end=" ")
        print()
        print("\033[32m",puntos_crupier, "Puntos\033[0m")
    
    def turno_jugador_bj():
        nonlocal cartas_jugador
        nonlocal casilleros_jugador
        nonlocal indice_mazo
        nonlocal opcion_bj
        
        opcion_bj = 1
        while puntos_jugador < 21 and opcion_bj != 2:
            print("\033[33m1. Pedir carta")
            print("2. Plantarse\033[0m")
            opcion_bj=int(input("Opcion: "))

            while opcion_bj != 1 and opcion_bj != 2:
                print("Opcion invalida, por favor ingrese una opcion valida")
                opcion_bj=int(input("Opcion: "))
            if opcion_bj == 1:
                cartas_jugador[casilleros_jugador]=mazo[indice_mazo]
                casilleros_jugador += 1
                indice_mazo += 1

                puntos_jugador_bj()
            
                os.system('cls')

                mostrar_puntos_jugador_bj()
                print()
                mostrar_puntos_crupier_bj()
     
    def turno_crupier_bj():
        nonlocal indice_mazo
        nonlocal casilleros_crupier
        nonlocal cartas_crupier
        
        while puntos_crupier < 17 and puntos_crupier < puntos_jugador:
            cartas_crupier[casilleros_crupier]=mazo[indice_mazo]
            casilleros_crupier += 1
            indice_mazo += 1
            
            puntos_crupier_bj()
        
        mostrar_puntos_jugador_bj()
        print()
        mostrar_puntos_crupier_bj()
    
    def ganador_bj():
        global victorias_bj
        
        if puntos_crupier > 21:
            print("Gana",jugador_bj)
            victorias_bj += 1
        
        elif puntos_jugador > 21:
            print("Gana la casa")
        
        elif puntos_jugador > puntos_crupier:
            print("Gana", jugador_bj)
            victorias_bj += 1
        
        elif puntos_crupier > puntos_jugador:
            print("Gana la casa")
        
        else:
            print("Empate")
        
    
    def volver_a_jugar_bj():
        nonlocal jugar_bj
        
        print("Partida finalizada!")
        jugar_bj = input("¿Queres voler a jugar? (si/no) ").lower()
        
        while jugar_bj != "si" and jugar_bj != "no":
            print("ERROR, introduzca una opcion valida")
            jugar_bj = input ("¿Queres voler a jugar?").lower()
        
        if jugar_bj == "no":
            print("\033[36m¡Gracias por jugar!\033[0m")
        
        if jugar_bj == "si":
            input("\033[36m'Enter' para repartir de nuevo \033[0m" )
            os.system('cls')

    def juego():
        nonlocal indice_mazo
        nonlocal casilleros_jugador
        nonlocal casilleros_crupier
        nonlocal puntos_jugador
        nonlocal puntos_crupier
        nonlocal ases_jugador
        nonlocal ases_crupier
        nonlocal cartas_jugador
        nonlocal cartas_crupier
        nonlocal jugar_bj
        global partidas_jugadas
        global victorias_bj
        
        while jugar_bj == "si":    
            partidas_jugadas += 1
            indice_mazo = 0
            casilleros_jugador = 0
            casilleros_crupier = 0
            puntos_jugador = 0
            puntos_crupier = 0
            ases_jugador = 0
            ases_crupier = 0
            cartas_jugador = [' '] * 8
            cartas_crupier = [' '] * 8
            

            
            mazo_bj()
            reparto_inicial_bj()

            puntos_jugador_bj()
            puntos_crupier_bj()

            mostrar_puntos_jugador_bj()
            print()
            mostrar_puntos_crupier_bj()
       
            turno_jugador_bj()
       
            if puntos_jugador <= 21:
                turno_crupier_bj()
        
            ganador_bj()
        
            volver_a_jugar_bj()

    introduccion_bj()
    juego()

def puntos():
    print("Partidas jugadas: ",partidas_jugadas)
    print("\033[32mPartidas ganadas: ",victorias_bj,"\033[0m")
         
blackjack()    
puntos()    