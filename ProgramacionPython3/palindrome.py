def es_palindromo(palabra):
    palabra = palabra.lower()  # Convertir la palabra a minúsculas para ignorar mayúsculas
    palabra = palabra.replace(" ", "")  # Eliminar espacios en blanco
    return palabra == palabra[::-1]  # Verificar si la palabra es igual a su inversa

palabra = input("Ingrese una palabra: ")
if es_palindromo(palabra):
    print("La palabra sí es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")
