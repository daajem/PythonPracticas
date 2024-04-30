import random

# Recibimos la cantidad de numeros que va a tener nuestro arreglo
cant = int(input('Ingresa la cantidad de numeros de la lista: '))

# Creamos una lista con números aleatorios del 1 al 100
numbers = [random.randrange(1, 100) for _ in range(cant)]

# Imprimimos el arreglo original
print("Arreglo original:", numbers)

# Mezclamos el arreglo utilizando random.shuffle()
random.shuffle(numbers)

# Imprimimos el arreglo mezclado
print("Arreglo mezclado:", numbers)
