# Programa que dice cual numero es mayor de una serie de numeros introducidos 
repetir = 's'

while repetir.lower() == 's':
    # Inicializar la variable para el número mayor
    mayor = None

    print("Introduce una serie de números enteros. Introduce 0 para terminar.")

    while True:
        # Pedir un número entero al usuario
        numero = int(input("Introduce un número: "))

        # Si el número es 0, salir del ciclo
        if numero == 0:
            break

        # Verificar si es el mayor número introducido hasta el momento
        if mayor is None or numero > mayor:
            mayor = numero

    # Mostrar el número mayor introducido
    if mayor is not None:
        print(f"El número mayor introducido fue: {mayor}")
    else:
        print("No se introdujeron números.")

    # Preguntar si el usuario desea repetir el proceso
    repetir = input("¿Quieres repetir el proceso? (s/n): ")

print("Programa finalizado.")
