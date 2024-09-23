# Tabla de multiplicar con for
import os

while True:
    os.system('clear')  # Asegúrate de que este comando funcione en tu entorno (por ejemplo, en Windows sería 'cls')
    print('Tabla de multiplicar con for \n')
    
    t = int(input('¿Qué tabla deseas? '))
    n = int(input('¿Hasta dónde la deseas? '))
    
    for i in range(1, n + 1):
        print(f'{t} x {i} = {t * i}')
    
    res = input('\n\n¿Deseas continuar (S/N)? ').upper()
    if res == 'N':
        break

print('Gracias por utilizar este programa')
