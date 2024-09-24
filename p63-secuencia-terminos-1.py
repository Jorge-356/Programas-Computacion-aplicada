# Se desea imprimir la secuencia de términos armónicos el numero de renglones que el usuario desee y su suma:
import math
n = int(input("¿Cuántos términos? "))

# Variable para acumular la suma
suma = 0

# Crear una lista para almacenar los términos y luego imprimirlos
terminos = []

# Ciclo para calcular los términos y la suma
for i in range(1, n + 1):
    # Calcular el término 1/i!
    termino = 1 / math.factorial(i)
    
    # Añadir el término a la lista para la salida
    terminos.append(f"1/{i}!")
    
    # Acumular la suma
    suma += termino

# Imprimir la secuencia de términos y la suma
print(" + ".join(terminos), f", suma: {suma}")
