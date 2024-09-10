# Programa que calcula la suma y el promedio de una serie de numeros ingresados
while True:
    # Inicializar las variables
    suma = 0
    contador = 0

    print("Introduce números enteros para calcular la suma y el promedio. Introduce 0 para terminar.")

    while True:
        # Pedir un número entero al usuario
        numero = int(input("Introduce un número entero: "))

        # Si el número es 0, salir del ciclo interno
        if numero == 0:
            break

        # Sumar el número y contar los números introducidos
        suma += numero
        contador += 1

    # Verificar si se introdujeron números
    if contador > 0:
        promedio = suma / contador
        print(f"Suma de los números: {suma}")
        print(f"Promedio de los números: {promedio}")
        print(f"Números introducidos: {contador}")
    else:
        print("No se introdujeron números.")

    # Preguntar si el usuario desea repetir el proceso
    repetir = input("¿Quieres repetir el proceso? (s/n): ")
    if repetir.lower() != 's':
        break

print("Programa finalizado.")
