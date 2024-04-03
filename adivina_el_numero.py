import random

def main():
    numero_secreto = random.randint(1 , 101)
    intentos = 0
    
    while True:
        
        suposicion = int(input("cual crees que es el numero? "))
        intentos += 1
        
        if suposicion < numero_secreto:
            print("el numero", suposicion,"no es el correcto intenta mas arriva")
            
        elif suposicion > numero_secreto:
            print("el numero", suposicion,"no es el correcto intenta mas abajo")
            
        else:
            print("el numero secreto era",numero_secreto)
            break

if __name__ == "__main__":
    print("***" * 5)
    print("Adivina el numero")
    print("del 1 al 100")
    print("***" * 5)
    
    
    main()
    print("fin")
    