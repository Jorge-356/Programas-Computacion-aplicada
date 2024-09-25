# Remover elementos de la lista

import os; os.system('cls')
nums = [1, 3, 5, 7, 9, 11, 99, 15, 88, 19, 100]
print(f'todos los números : {nums}\n')
nums.remove(99)
print(f'remover primera ocurrencia : {nums}\n')
num=nums.pop(8)
print(f'remover y regresar elemento : {nums} - {num}\n')
num=nums.pop()
print(f'remover el ultimo: : {nums} - {num}\n')
nums.clear()
print(f'remover todos : {nums}\n')