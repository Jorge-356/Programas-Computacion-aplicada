# Función para leer una lista de números enteros
def leer_lista():
    # Se solicita al usuario que ingrese los números
    numeros = input("Dame los números: ")
    # Convertir la cadena de entrada en una lista de enteros
    lista_numeros = list(map(int, numeros.split()))
    return lista_numeros

# Función para calcular el factorial de un número
def calcular_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n+1):
            factorial *= i
        return factorial

# Función que recibe la lista, calcula el factorial de cada número y devuelve la lista con los factoriales
def calcular_factoriales(lista_numeros):
    lista_factoriales = []
    for numero in lista_numeros:
        lista_factoriales.append(calcular_factorial(numero))
    return lista_factoriales

# Función principal que imprime las listas
def main():
    # Leer la lista de números
    lista_numeros = leer_lista()
    # Calcular los factoriales de la lista
    lista_factoriales = calcular_factoriales(lista_numeros)
    # Imprimir las listas
    print("La lista de números originales:", lista_numeros)
    print("La lista con los factoriales:", lista_factoriales)

# Llamada a la función principal
main()
