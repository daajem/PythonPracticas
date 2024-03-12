def calculoTip(total, porcentaje):
    cTotal = total * (porcentaje / 100)
    return cTotal

total = float(input("Ingresar el total de la cuenta: "))
porcentaje = float(input("Ingresa el porcentaje de propina que deseas dar: "))
print(f"La propina a pagar es: ${calculoTip(total, porcentaje):.2f}")