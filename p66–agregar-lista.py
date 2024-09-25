# Agregar elementos a la lista
import os
os.system('cls')

print('Agregar elementos a una lista existente \n')

# Definir la lista inicial de números
nums = [80.3, 12.5, 60.2, 30.4]

# Mostrar todos los números iniciales
print(f'Todos los números: {nums}\n')

# Agregar elementos al final de la lista
nums.append(90)
nums.append(100)
print(f'Agregar al final: {nums}\n')

# Insertar un número en el índice 4
nums.insert(4, 80)
print(f'Insertar el número 80 en el índice 4: {nums}\n')

# Extender la lista con otra lista
otros = [110, 120, 130]
nums.extend(otros)
print(f'Extender con {otros}: {nums}\n')
