import random

def adivinar_numero():
    print("Piensa en un número del 1 al 100. Yo intentaré adivinarlo.")
    print("Después de cada intento, dime si estoy 'caliente' o 'frio'.")

    limite_inferior = 1
    limite_superior = 100
    intentos = 0

    while True:
        intento = random.randint(limite_inferior, limite_superior)
        respuesta = input(f"¿Estoy caliente o frio con {intento}? ")

        if respuesta.lower() == "caliente":
            print("¡Estoy cerca!")
        elif respuesta.lower() == "frio":
            print("Necesito ajustar mi suposición.")
            limite_inferior = intento + 1
        else:
            print("Respuesta no válida. Por favor, responde con 'caliente' o 'frio'.")

        if limite_inferior > limite_superior:
            print("¡No debería haber pasado esto! Reiniciando...")
            limite_inferior = 1
            limite_superior = 100
            intentos = 0
            continue

        if limite_inferior == limite_superior:
            print(f"¡Tu número es {limite_inferior}! ¡Adiviné en {intentos} intentos!")
            break

        intentos += 1

adivinar_numero()
