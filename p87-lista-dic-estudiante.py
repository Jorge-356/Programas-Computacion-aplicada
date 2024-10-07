# Estudiantes y sus datos, en una Lista de Diccionarios
import os
os.system('cls')

# Lista inicial de estudiantes
grupo = [
    {'nombre': 'Carlos', 'edad': 45, 'carrera': 'sistemas', 'promedio': 9},
    {'nombre': 'Rocio', 'edad': 35, 'carrera': 'sistemas', 'promedio': 10}
]

print(f'Grupo original: {grupo}')

# Bucle para agregar nuevos estudiantes
while True:
    print(f'\nDatos Estudiante:')
    datos = {}
    nombre = input('Nombre? ')
    if nombre != '':
        datos['nombre'] = nombre
        datos['edad'] = int(input('Edad? '))
        datos['carrera'] = input('Carrera? ')
        datos['promedio'] = float(input('Promedio? '))
        grupo.append(datos)
    else:
        break

# Mostrar el grupo completo de estudiantes
print(f'\nGrupo completo: {grupo} - Total de estudiantes: {len(grupo)}')

# Mostrar datos en forma de tabla
print('\nDatos en forma de Tabla:\n')
for k in grupo[0].keys():  # Mostrar los títulos de la tabla
    print(f'{k}\t', end='')
print()  # Nueva línea después de los títulos

for alumno in grupo:  # Mostrar los datos de cada estudiante en filas
    for v in alumno.values():
        print(f'{v}\t', end='')
    print()  # Nueva línea para cada estudiante

# Mostrar datos en forma de registro
print('\nDatos en forma de Registro:\n')
s = 0  # Variable para la suma de los promedios
for est in grupo:
    s += est['promedio']  # Sumar los promedios de cada estudiante
    for k, v in est.items():  # Mostrar cada clave y valor del estudiante
        print(f'{k:<10} : {v}')
    print('')  # Nueva línea después de cada estudiante

# Calcular y mostrar el promedio general
p = s / len(grupo)
print(f'La suma de los promedios es: {s}')
print(f'El promedio general es: {p:.2f}')
