import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # 'cls' para Windows, 'clear' para Linux/Mac
    t = int(input('¿Qué tabla quieres? '))
    n = int(input('¿Hasta dónde la quieres? '))
    
    c = 1
    while c <= n:
        print(f'{t} x {c} = {t * c}')
        c += 1  # Asegúrate de incrementar 'c' dentro del bucle

    res = input('¿Deseas continuar (S/N)? ')
    if res.upper() == 'N':
        break

print("Gracias por utilizar este programa...")
