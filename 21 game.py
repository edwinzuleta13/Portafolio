#Se importa la libreria Random
import random

# Definir las cartas y sus valores
cartas = [
    {"carta": "2", "valor": 2},
    {"carta": "3", "valor": 3},
    {"carta": "4", "valor": 4},
    {"carta": "5", "valor": 5},
    {"carta": "6", "valor": 6},
    {"carta": "7", "valor": 7},
    {"carta": "8", "valor": 8},
    {"carta": "9", "valor": 9},
    {"carta": "10", "valor": 10},
    {"carta": "J", "valor": 10},
    {"carta": "Q", "valor": 10},
    {"carta": "K", "valor": 10},
    {"carta": "A", "valor": 11}  
]


#Valor total es una funcin que calcula los ases en una lista y dependiado de el valor todal de la suma, reduce el valor de los ases

def valor_total(cartas):
    suma = sum(cartas)
    num_ases = cartas.count(11)
    while suma > 21 and num_ases:
        suma -= 10
        num_ases -= 1
    return suma


def dar_cartas(cartas):
    
    #Se copia la lista cartas para no modificar esta misma
    baraja = cartas.copy()
    
    #Shuffle mueve el orden de la lista
    random.shuffle(baraja)
    mano_jugador = []
    
    # Repartir dos cartas iniciales
    for _ in range(2):
        carta = baraja.pop()
        mano_jugador.append(carta)
    
    # Mostrar las cartas iniciales
    print("Tus cartas iniciales son:")
    for carta in mano_jugador:
        print(carta)
        
    #se llama a la funcion valor todal y se hace un ciclo for en la lista mano jugador solo calculando el "valor"
    suma_jugador = valor_total([carta['valor'] for carta in mano_jugador])
    
    # Preguntar si desea agregar otra carta
    while True:
        Si_No = input("¿Quieres agregar otra carta? (S/N): ")
        if Si_No.lower() == "s":
            
            #pop se usa para selecionar la carta anterior y eliminarla colocando por encima la sigienta carta
            carta = baraja.pop()
            
            #append agrega la carta eliminada a la variable temporal
            mano_jugador.append(carta)
            
            #se llama de nuevo a la funcion valor total
            suma_jugador = valor_total([carta['valor'] for carta in mano_jugador])
            
            print(f"Has añadido una carta con valor: {carta['valor']}")
            
            if suma_jugador > 21:
                print("Te has pasado de 21. ¡Has perdido!")
                return
        else:
            break
        print("\nTus cartas finales son:")
        for carta in mano_jugador:
            print(carta)
    print(f"El valor total de tus cartas es: {suma_jugador}")
    
#------------------Empieza el codigo para la computadora------------------

    mano_computadora = []
    
    # Repartir dos cartas iniciales
    for _ in range(2):
        carta = baraja.pop()
        mano_computadora.append(carta)
    
    print("\nCartas de la computadora:")
    for carta in mano_computadora:
        print(f"{carta['carta']} (valor: {carta['valor']})")
    
    suma_computadora = valor_total([carta['valor'] for carta in mano_computadora])
    #Se usa el ciclo while para determinar si la suma de la coputadora el mayor a 17
    while suma_computadora < 17:
        carta = baraja.pop()
        mano_computadora.append(carta)
        suma_computadora = valor_total([carta['valor'] for carta in mano_computadora])
    
    print("\nCartas finales de la computadora:")
    
    for carta in mano_computadora:
        print(f"{carta['carta']} (valor: {carta['valor']})")
    print(f"El valor total de las cartas de la computadora es: {suma_computadora}")
    
    #Se determina el ganador
    if suma_jugador == 21:
        print("ganaste")
    elif suma_computadora > 21:
        print("La computadora se ha pasado de 21. ¡Ganaste!")
    elif suma_jugador > 21 or suma_computadora > suma_jugador:
        print("La computadora gana.")
    elif suma_jugador < suma_computadora:
        print("La computadora gana.")
    elif suma_computadora > suma_jugador:
        print("computadora gana")
    else:
        print("¡Es un empate!")


# Ejemplo de uso
dar_cartas(cartas)

    

        
        













