

import random

def play_rps(user_choice):
    options = ["Piedra", "Papel", "Tijeras"]
    computadoraEscoge = random.choice(options)

    if user_choice == computadoraEscoge:
        return "Empate"
    elif (user_choice == "Piedra" and computadoraEscoge == "Tijeras") or (user_choice == "Papel" and computadoraEscoge == "piedra") or (user_choice == "tijeras" and computadoraEscoge == "papel"):
        return f"Ganaste. La computadora escogio: {computadoraEscoge}."
    else:
        return f"Perdiste. La computadora escogio: {computadoraEscoge}."

user_input = input("Elige piedra, papel o tijeras: ").lower()
print(play_rps(user_input))