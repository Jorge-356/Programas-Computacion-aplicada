import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla según el sistema operativo
    n = int(input('¿Hasta qué tabla quieres? '))
    m = int(input('¿Hasta dónde la quieres? '))

    t = 1
    while t <= n:
        print(f'\nTabla del {t}\n')  # Imprime la cabecera de la tabla
        c = 1
        while c <= m:
            print(f'{t} x {c} = {t * c}')  # Imprime la multiplicación
            c += 1
        t += 1

    res = input('\n¿Deseas continuar (S/N)? ')
    if res.upper() == 'N':  # Termina el bucle si la respuesta es 'N'
        break

print("\nGracias por utilizar este programa...")
