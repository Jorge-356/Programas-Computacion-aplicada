# Sumar e imprimir 2 listas de n números
import os
os.system('clear')

print('Sumar e imprimir 2 listas de n números\n')

c = int(input('¿Cuántos elementos? '))

# Lectura de la Lista 1
print('\nLeyendo los elementos de la Lista 1:')
lista1 = []
for i in range(c):
    n = int(input(f'Lista1[{i}]: '))
    lista1.append(n)

print(f'\nLista1: {lista1}')

# Lectura de la Lista 2
print('\nLeyendo los elementos de la Lista 2:')
lista2 = []
for i in range(c):
    n = int(input(f'Lista2[{i}]: '))
    lista2.append(n)

print(f'\nLista2: {lista2}')

# Calculando e imprimiendo la suma de las listas
print('\nCalculando e imprimiendo la suma de las listas')
lista3 = []
for i in range(c):
    lista3.append(lista1[i] + lista2[i])

print(f'\nLista3 (Suma de Lista1 y Lista2): {lista3}')
