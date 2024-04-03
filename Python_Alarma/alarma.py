from time import localtime
from pygame import mixer

while True:
    H = input("Ingrese la hora: ")
    M = input("Ingrese el minuto: ")

    # Validar que las entradas sean números enteros
    if H.isdigit() and M.isdigit():
        H = int(H)
        M = int(M)
        break
    else:
        print("Por favor, ingrese valores numéricos para la hora y el minuto.")

while True:
    if localtime().tm_hour == H and localtime().tm_min == M:
        print("Sonando alarma")
        mixer.init()
        mixer.music.load('alar.mp3')
        mixer.music.play()
        break