# Imprimer los numeros imapares hasta N numero, ademas da la suma de estos

while True:
    # Pedir al usuario un número entero positivo
    n = int(input("Introduce un número positivo para imprimir los números impares hasta ese número: "))

    # Inicializar la suma y el contador
    suma_impares = 0
    i = 1

    print("Números impares:")
    
    # Ciclo para imprimir los números impares y sumar
    while i <= n:
        if i % 2 != 0:  # Verificar si es impar
            print(i, end=" ")
            suma_impares += i
        i = i +1 

    print("\nSuma de los números impares:", suma_impares)

    # Preguntar si desea repetir el proceso
    repetir = input("¿Quieres repetir el proceso? (s/n): ")
    if repetir.lower() != 's':
        break

print("Programa finalizado.")
