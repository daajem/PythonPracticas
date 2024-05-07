def prime(num): # Funcion para reconocer los numeros que sean primos
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def printTriangle(numero): # Funcion que nos permite ingresar el numero y imprimirlo en forma de triangulo 
    if numero < 2 or not prime(numero):
        print("El número ingresado no es un número primo.")
        return
    
    for i in range(numero, 0, -1):
        fila = []
        for j in range(i, 0, -1):
            if prime(j):
                fila.append(str(j))
        print(" ".join(fila))

numero = int(input("Ingrese un número entero primo: "))
printTriangle(numero)
