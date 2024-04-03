import random

numbers = "1234567890qwertyuiop+asdfghjklñ<zxcvbnm,.-"
 
passwords = int(input("cuantas contraseñas quieres generar?: "))
longitud = int(input("de cuantos numeros sera tu contraseña?: "))


for _ in range(passwords):
    password = ""
    for _ in range(longitud):
        password += random.choice(numbers)
    print(password)
    print("fin")
        