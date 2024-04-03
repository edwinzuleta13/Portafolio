import random
def main():
    intentos = 0
    win = 1
    lose = 1
    print("**********")
    print("1 = piedra")
    print("2 = papel")
    print("3 = tijera")
    print("**********")
    
    while True:
        jugador = int(input("escoje tu material?: \n"))
        intentos += 1
        computadora = random.randint(1,3)
        
        if win == 5:
            print("ganaste")
            break
        elif lose == 5:
            print("perdiste")
            break
        #jugador gana
        
        elif jugador == 1 and computadora == 3:
            print("sacaste piedra y la computadora tijera\n")
            print("ganaste", win,"rondas llega a 5 para ganar\n")
            win += 1
            
        elif jugador == 2 and computadora == 1:
            print("sacaste papel y la computadora piedra\n")
            print("ganaste", win,"rondas llega a 5 para ganar\n")
            win += 1
            
        elif jugador == 3 and computadora == 2:
            print("sacaste tijera y la computadora papel\n")
            print("ganaste", win,"rondas llega a 5 para ganar\n")
            win += 1
        
        #jugador pierde
        
        elif computadora == 1 and jugador == 3:
            print("sacaste piedra y la computadora papel\n")
            print("perdiste", lose,"rondas si pierdes 5 se acaba el juego\n")
            lose += 1
            
            
        elif computadora == 2 and jugador == 1:
            print("sacaste papel y la computadora tijera\n")
            print("perdiste", lose,"rondas si pierdes 5 se acaba el juego\n")
            lose += 1
            
        elif computadora == 3 and jugador == 2:
            print("sacaste papel y la computadora tijera\n")
            print("perdiste", lose,"rondas si pierdes 5 se acaba el juego\n")
            lose += 1
        
        #empates
        
        elif jugador == 1 and computadora == 1:
            print("empate\n")
        elif jugador == 2 and computadora == 2:
            print("empate\n")
        elif jugador == 3 and computadora == 3:
            print("empate\n")
        elif computadora == 1 and jugador == 1:
            print("empate\n")
        elif computadora == 2 and jugador == 2:
            print("empate\n")
        elif computadora == 3 and jugador == 3:
            print("empate\n")

            
            
if __name__ == "__main__":
    print("****" * 5)
    print("piedra papel o tijera")
    print("****" * 5)
    main()
    print("fin")