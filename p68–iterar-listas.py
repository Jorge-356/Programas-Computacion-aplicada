# Iterar sobre los elementos de la lista

# Limpiar la pantalla (solo en sistemas Unix, como Linux o macOS)
import os
os.system('clear')

# Definir la lista de números
nums = [2, 4, 6, 8, 10, 12, 14, 16]
print(f'Todos los números: {nums}\n')

# Iterar por elementos de la lista
print('Iterar por elementos:')
for n in nums:
    print(n)

# Iterar por índice de la lista
print('\nIterar por índice:')
for i in range(len(nums)):
    print(nums[i])

# Iterar por elementos y sumar 2 a cada elemento
print('\nIterar por elementos sumando 2:')
for n in nums:
    print(n + 2)

# Iterar por índice y sumar 10 al valor correspondiente
print('\nIterar por índice sumando 10:')
for i in range(len(nums)):
    print(nums[i] + 10)
