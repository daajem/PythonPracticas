def palindromo(palabra):
    palabraL = palabra.lower().replace(" ", "")
    return palabraL  == palabraL [::-1]

cPalabra = input("Ingresa una palabra o frase: ")
if palindromo(cPalabra):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")