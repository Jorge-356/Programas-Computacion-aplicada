while True:
    # Pedir al usuario un número entero positivo
    n = int(input("Introduce un número menor que 100 para imprimir los números pares desde 100 hasta ese número: "))

    # Verificar que el número ingresado sea menor que 100
    if n >= 100:
        print("Por favor, introduce un número menor que 100.")
        continue

    # Inicializar la suma y el contador
    suma_pares = 0
    i = 100

    print("Números pares:")
    
    # Ciclo para imprimir los números pares y sumar
    while i >= n:
        if i % 2 == 0:  # Verificar si es par
            print(i, end=" ")
            suma_pares = suma_pares + i
        i =  i - 1

    print(f"\nSuma de los números pares: {suma_pares}")

    # Preguntar si desea repetir el proceso
    repetir = input("¿Quieres repetir el proceso? (s/n): ")
    if repetir.lower() != 's':
        break

print("Programa finalizado.")
