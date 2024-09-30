# Dado un día, imprimir la paga correspondiente
import os
os.system('cls')

print('Dado un día, imprimir la paga correspondiente\n')

dias = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
paga = [100, 200, 300, 400, 500, 600, 700]

# Solicitar el día al usuario
while True:
    dia = input('Dame un día entre lunes y domingo: ').lower()
    if dia in dias:
        break
    else:
        print('Día inválido, por favor intenta nuevamente.')

# Mostrar el día y la paga correspondiente
print(f'Elegiste el día: {dia}')
pos = dias.index(dia)
print(f'Que corresponde a una paga de: {paga[pos]}')
