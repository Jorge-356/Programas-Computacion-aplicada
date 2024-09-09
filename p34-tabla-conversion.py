import os

while True:
    os.system('clear')  # Limpia la pantalla (en sistemas basados en Unix como Linux o MacOS)
    tc = 20.71  # Tipo de cambio de peso a dólar
    pi = float(input("Valor inicial en pesos: "))
    pf = float(input("Valor final en pesos: "))
    
    c = pi
    print("\nPesos\tDollar")
    print("-" * 15)
    
    # Ciclo para realizar la conversión de cada valor dentro del rango
    while c <= pf:
        print(f'{c:.2f}\t{c/tc:.2f}')  # Impresión con dos decimales
        c += 1  # Incrementa en 1 el valor de c
    
    print("-" * 15)
    
    # Pregunta si desea continuar
    res = input('Deseas continuar (S/N)? ')
    if res.upper() == 'N':  # Si la respuesta es 'N' o 'n', termina el bucle
        break
