# Lista con 2 diccionarios
autos = [
    {'marca': 'Ford', 'modelo': 'Mustang', 'año': 1964},
    {'marca': 'VW', 'modelo': 'Jetta', 'año': 2015}
]

# Agregar elemento al diccionario
autos.append({'marca': 'Ford', 'modelo': 'Focus', 'año': 2000})

# Mostrar todos los autos y el número de autos
print('\nTodos los autos:', autos, len(autos))

# Mostrar cada auto dentro de la lista de autos
print('\nCada auto dentro de los autos:\n')
for auto in autos:
    print(auto)

# Mostrar datos en forma de tabla
print('\nDatos en forma de Tabla:\n')
for k in autos[0].keys():  # títulos de la tabla
    print(f'{k}\t', end='')
print()  # Nueva línea después de los títulos

for auto in autos:  # para cada auto
    for v in auto.values():  # imprime sus valores
        print(f'{v}\t', end='')
    print()  # Nueva línea para cada auto

# Mostrar datos en forma de registro
print('\nDatos en forma de Registro\n')
for auto in autos:  # para cada auto
    for k, v in auto.items():  # imprime sus llaves y valores
        print(f'{k:<12} : {v}')
    print('')  # Nueva línea después de cada auto
