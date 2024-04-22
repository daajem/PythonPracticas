# Lista de las denominaciones de monedas disponibles
denominations = [20, 10, 5, 1]

# Lista para almacenar la cantidad de cada tipo de moneda
coins = [0, 0, 0, 0]

# Solicitar al usuario la cantidad de dinero a convertir
amount = int(input('Ingresa la cantidad de dinero a convertir: '))

# Iterar sobre cada denominación de moneda
for i, coin in enumerate(denominations):
    # Verificar si la cantidad es mayor o igual que la denominación actual
    if amount >= coin:
        # Calcular la cantidad de esta moneda necesaria y actualizar la cantidad restante
        coins[i] = amount // coin
        amount %= coin

# Mostrar la cantidad de cada tipo de moneda y el cambio sobrante
print('La cantidad de monedas son:\nMonedas de $20: {}\nMonedas de $10: {}\nMonedas de $5: {}\nMonedas de $1: {}\nSobra ${}'.format(coins[0], coins[1], coins[2], coins[3], amount))
