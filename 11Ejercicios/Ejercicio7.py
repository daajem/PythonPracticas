import random

def guess_the_number():
    numberSecret = random.randint(1, 100)
    intentos = 0

    while True:
        user_guess = int(input("Adivina el número (entre 1 y 100): "))
        attempts += 1

        if user_guess == numberSecret:
            print(f"Correcto El número era {numberSecret}. Necesitaste {intentos} intentos.")
            break
        elif user_guess < numberSecret:
            print("Intenta con un número más grande.")
        else:
            print("Intenta con un número más pequeño.")

guess_the_number()