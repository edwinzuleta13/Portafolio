import random

print("Bienvenido a Unlikely")
print("-----REGLAS-----")
print("1. El juego te proporcionará 9 cartas, en las cuales te saldrán tres números al azar")
print("2. Tendrás que lanzar tres dados; si los números de los dados coinciden con los de las cartas, se sumará 1 punto")
print("3. Si llegas a 10 puntos, ganas. En cambio, si no llegas a la cantidad pedida, pierdes")

def mostrar_cartas():
    car1 = random.randint(1, 6)
    car2 = random.randint(1, 6)
    car3 = random.randint(1, 6)
    return car1, car2, car3

def lanzar_dado():
    dad1 = random.randint(1, 6)
    dad2 = random.randint(1, 6)
    dad3 = random.randint(1, 6)
    return dad1, dad2, dad3

def main():
    cartas = 9
    puntos = 0
    si_o_no = input("¿Quieres jugar? (s/n): ")
    if si_o_no.lower() != "s":
        return

    while puntos < 10 and cartas > 0:
        input("Presiona Enter para continuar...")

        print("Puntos:", puntos)
        print("Cartas:", cartas)
        input("Presiona Enter para mostrar tus cartas...")

        resultado_cartas = mostrar_cartas()
        print("El número de tus cartas son:", resultado_cartas)
        resultado_dados = lanzar_dado()
        print("Los dados han caído en los números:", resultado_dados)

        puntos_ganados = 0
        for carta, dado in zip(resultado_cartas, resultado_dados):
            if carta == dado:
                puntos_ganados += 1

        puntos += puntos_ganados
        if puntos_ganados > 0:
            print(f"Ganaste {puntos_ganados} punto(s)")

        print("Puntos:", puntos)
        cartas -= 1
        print("Cartas restantes:", cartas)

    if puntos >= 10:
        print("¡Has ganado!")
    else:
        print("¡Has perdido!")

if __name__ == "__main__":
    main()