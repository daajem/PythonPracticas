def c_Palabras(texto):
    palabras = texto.split()
    return len(palabras)

texto_Usuario = input("Ingresa una oración: ")
print(f"La oración tiene {c_Palabras(texto_Usuario)} palabras")