def printTriangle(hight): 
    for i in range(1, hight + 1):
        print('*' * i)

try:
    hight = int(input("Introduce la altura del triángulo: "))
    printTriangle(hight)
except ValueError:
    print("Por favor, introduce un número entero válido.")
