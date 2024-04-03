def informacion_correo(correo):
    partes = correo.split(".")
    return partes[0]


if __name__ == "__main__":
    print("Ejemplo: name.secondname@gmail.com")
    correo_electronico = input("Escribe tu correo electrónico: ")
     
    resultado = informacion_correo(correo_electronico)
    print(f"hola {resultado} tu correo se agrego con exito")
    print("fin")