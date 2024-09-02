print('Universad Autonoma De Zacatecas')
nombre = input('Dame tu nombre: ')
edad = int(input('Dame tu edad: '))

if edad < 18:
    print('Solo aceptamos mayores de 18.')
else:
    print('Dame 2 calificaciones:')
    c1, c2 = int(input()), int(input())
    if c1 < 8 or c2 < 8:
        print('Solo aceptamos alumnos con calificaciones mayores a 8.')
    else:
        print(f'{nombre}, bienvenid@ a la Universidad Patito. Tu edad {edad} y calificaciones {c1} y {c2} lo permiten.')
