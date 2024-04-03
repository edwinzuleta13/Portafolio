
def contar_palabras(frase):
    palabras = frase.split()
    return len(palabras)


if __name__ == "__main__":
    texto = input("escribe tus palabras: ")
    
    resultado = contar_palabras(texto)
    print(f"El número de palabras en la frase es: {resultado}")
    print("fin")