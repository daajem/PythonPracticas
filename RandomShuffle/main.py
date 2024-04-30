import random

def shuffle(arr):
    for i in range(len(arr) - 1, 0, -1):
        j = random.randint(0, i)  # Generamos un índice aleatorio entre 0 e i (ambos inclusive)
        arr[i], arr[j] = arr[j], arr[i]  # Intercambiamos los elementos en las posiciones i y j
    return arr

# Ejemplo de uso
letters = ['a', 'b', 'c']
print(f"Original: {letters}")

shuffled_letters = shuffle(letters)
print(f"Shuffle: {shuffled_letters}")
