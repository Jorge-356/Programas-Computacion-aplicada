# Imprime las tablas de la tabla 1 a la tabla n
import os
print('Imprime las tablas de la tabla 1 a la tabla n')
os.system('cls')  

n = int(input('¿Hasta qué tabla quieres? '))
m = int(input('¿Hasta dónde las deseas? '))

for i in range(1, n + 1):
    print(f'\nTabla del {i}:')  # Añadido para mayor claridad
    for j in range(1, m + 1):
        print(f'{i} x {j} = {i * j}')
    print('\n')  # Espacio entre tablas
