# Acceder a los elementos de una lista

# Limpiar la pantalla (solo en sistemas Unix, como Linux o macOS)
import os
os.system('clear')

# Definir la lista de números
nums = [10, 20, 30, 40, 60, 70, 10, 20, 99]

# Imprimir la cantidad de elementos en la lista
print('Acceder a los elementos de una lista\n')
print(f'Cantidad de números: {len(nums)} \n')

# Imprimir todos los elementos de la lista
print(f'Todos los números: {nums} \n')

# Imprimir el primer y último elemento de la lista
print(f'Primero y último número: {nums[0]}, {nums[-1]} \n')

# Imprimir los elementos desde el índice 2 hasta el 5 (recordando que el último índice no se incluye)
print(f'Del índice 2 al 5: {nums[2:6]} \n')

# Imprimir los primeros 3 elementos de la lista
print(f'Los primeros 3 números: {nums[:3]} \n')

# Imprimir los últimos 3 elementos de la lista
print(f'Los últimos 3 números: {nums[-3:]} \n')
