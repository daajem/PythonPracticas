def emailRebanado():
    correo = input("Ingresa tu dirección de correo electrónico: ").strip()
    usuario = correo[:correo.index('@')]
    dominio = correo[correo.index('@') + 1:]
    print(f"Nombre de usuario es: {usuario} \n Y el dominio es: {dominio}")

emailRebanado()