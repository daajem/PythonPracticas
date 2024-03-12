def solicitar_informacion(pregunta):
    while True:
        respuesta = input(pregunta)
        if respuesta.strip():  
            return respuesta.strip()
        else:
            print("Por favor, ingresa una respuesta válida.")

nombre = solicitar_informacion("¿Cuál es tu nombre? ")
fecha_nacimiento = solicitar_informacion("¿Cuál es tu fecha de nacimiento? (Formato: DD/MM/AAAA) ")
direccion = solicitar_informacion("¿Cuál es tu dirección? ")
metas_personales = solicitar_informacion("¿Cuáles son tus metas personales? ")

print("\nResumen de la información ingresada:")
print(f"- Nombre: {nombre}")
print(f"- Fecha de nacimiento: {fecha_nacimiento}")
print(f"- Dirección: {direccion}")
print(f"- Metas personales: {metas_personales}")