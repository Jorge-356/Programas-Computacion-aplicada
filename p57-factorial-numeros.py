# Imprime el factorial de n números

print('Calcula el factorial de n números:\n')
n = int(input('¿Cuántos números? '))

for num in range(1, n + 1):
    f = 1
    print(f'{num}! = ', end='')
    for i in range(1, num + 1):
        f *= i
    print(f)
