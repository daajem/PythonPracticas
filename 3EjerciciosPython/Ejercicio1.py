amoun_pay = float(input('Salario del empleado: '))
points = int(input('Cantidad de puntos del empleado: '))

pay = amoun_pay * (points / 10)

# Definir los rangos y niveles de rendimiento en un diccionario
performance_levels = {
    range(0, 3): 'Inaceptable',
    range(4, 7): 'Aceptable',
    range(7, 11): 'Meritorio'
}

# Determinar el nivel de rendimiento del empleado
level = None
for point_range, performance in performance_levels.items():
    if points in point_range:
        level = performance
        break

if level is None:
    level = "Nivel no definido"

print('Nivel de rendimiento "{}", Cantidad de dinero recibido ${}'.format(level, pay))
