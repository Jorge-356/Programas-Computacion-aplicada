
# suma cantidades x siempre y cuando no pase de 200
while True:
    # Inicializar las variables
    suma = 0
    contador = 0

    print("Introduce números enteros para sumarlos hasta que la suma sea >= 200.")

    while suma < 200:
        # Pedir un número entero al usuario
        numero = int(input("Introduce un número entero: "))

        # Sumar el número y contar los números introducidos
        suma += numero
        contador += 1

    # Mostrar la cantidad de números introducidos y la suma
    print(f"Suma total de los números: {suma}")
    print(f"Números introducidos: {contador}")

    # Preguntar si el usuario desea repetir el proceso
    repetir = input("¿Quieres repetir el proceso? (s/n): ")
    if repetir.lower() != 's':
        break

print("Programa finalizado.")
