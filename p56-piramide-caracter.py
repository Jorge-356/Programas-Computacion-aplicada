# Imprime pirámide de un caracter determinado
print('Imprime pirámide de un caracter determinado \n')

n = int(input('¿Cuántos renglones? '))
car = input('¿Caracter? ')

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(car, end='')
    print()  # Esta línea hace que pase al siguiente renglón
