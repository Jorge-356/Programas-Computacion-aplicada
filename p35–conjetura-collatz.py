import os

while True:
    os.system('cls') 
    print('Imprime la conjetura de Collatz')
    num = int(input('Dame un número: '))
    
    # Imprime la secuencia de la conjetura de Collatz
    while num != 1:
        print(num, end=' ')
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
    
    print(num)  # Imprime el último número que será 1
    
    # Pregunta si desea continuar
    res = input('\n¿Deseas continuar (S/N)? ')
    if res.upper() == 'N':  # Termina el bucle si la respuesta es 'N'
        break
