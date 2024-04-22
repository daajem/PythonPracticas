amount = float(input('¿Cantidad a invertir? '))
inter = float(input('¿Interés porcentual anual?'))
input_year = int(input('¿Años?: '))

for year in range(1, input_year + 1):
    amount += amount * (inter / 100)
    print('Capital tras el año {year}: {money}'.format(year, amount))