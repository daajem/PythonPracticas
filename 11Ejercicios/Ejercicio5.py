def generadorAcronimo(frase):
    palabras = frase.split()
    acronimo = "".join(palabra[0].upper() for palabra in palabras)
    return acronimo

palabra_completa = input("Ingresa la frase")
print(f"El acrónimo es: {generadorAcronimo(palabra_completa)}")