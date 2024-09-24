# Se desea imprimir la secuencia de números según el número de renglones que el usuario desee

# Pedir al usuario un número
n = int(input("Dame un número: "))

# Ciclo para cada línea
for i in range(1, n + 1): 
    # Ciclo para imprimir los números de 1 hasta i en la misma línea
    for j in range(1, i + 1):
        print(j, end=" ") 
    print()
