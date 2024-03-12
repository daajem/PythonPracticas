def odd_or_even():
    
    print("Bienvenido!, Al juego  de Impar o Par")

    while True:
        
        number = input("Por favor de ingresar de 1 a 1000:")

        
        if number.lower() == 'salir':
            print("Gracias por jugar")
            break

        
        if not number.isdigit():
            print("Numero no valido")
            continue

        
        number = int(number)

        
        if number % 2 == 0:
            print(f"{number} Numnero par")
        else:
            print(f"{number} Numero impar")

odd_or_even()
