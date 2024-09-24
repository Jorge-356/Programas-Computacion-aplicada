# Se desea imprimir la secuencia de números mostrados el numero de renglones que el usuario desee:
n = int(input("Dame un número: "))

# Ciclo para cada línea
for i in range(1, n + 1):
    # Ciclo para imprimir el número `i`, `i` veces en la misma línea
    for j in range(i):
        print(i, end=" ")
    # Saltar a la siguiente línea después de imprimir el número `i` veces
    print()
