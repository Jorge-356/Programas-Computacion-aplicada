# Imprime el factorial de un número
print('Imprime el factorial de un número \n')
n = int(input('¿De qué número deseas el factorial? '))
f = 1

for i in range(1, n + 1):
    f = f * i

print(f'\nEl factorial de {n} es: {f}')
