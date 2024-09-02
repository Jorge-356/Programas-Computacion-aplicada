print('Calculando los valores de la segunda ley de Newton')
print('[1] Calcular la fuerza')
print('[2] Calcular la masa')
print('[3] Calcular la aceleración')

op = int(input('Elige una opción: '))

if op == 1:
    print('\nCalculando la fuerza...')
    m = int(input('Dame la masa: '))
    a = int(input('Dame la aceleración: '))
    f = m * a
    print(f'La fuerza es {f}')
elif op == 2:
    print('\nCalculando la masa...')
    f = int(input('Dame la fuerza: '))
    a = int(input('Dame la aceleración: '))
    m = f / a
    print(f'La masa es {m}')
elif op == 3:
    print('\nCalculando la aceleración...')
    f = int(input('Dame la fuerza: '))
    m = int(input('Dame la masa: '))
    a = f / m
    print(f'La aceleración es {a}')
else:
    print('Tecleale bien')

