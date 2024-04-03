import datetime
import time

hora_actual = datetime.datetime.now().strftime("%H:%M")

hora_alarma = input("Ingrese la hora de la alarma (HH:MM): ")

def verificar_hora(hora_actual, hora_alarma): 
    if hora_actual == hora_alarma: 
        print("¡Es hora de la alarma!")

while True:
    hora_actual = datetime.datetime.now().strftime("%H:%M")
    verificar_hora(hora_actual, hora_alarma)

    print("fin")

  


