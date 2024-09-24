# Se desea imprimir los números de 1 a n de 10 en 10
n = int(input("Dame un número: "))

# Variable para controlar el incremento de 10 en 10
i = 1

# Usar un ciclo for sin range
for _ in range(n):
    if i > n:
        break
    print(i, end=" ")
    i += 10
