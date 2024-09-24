# Se desea imprimir los pares de 2 a n y su suma
n = int(input("Dame un número: "))

# Variable para acumular la suma
suma = 0

# Inicializamos en 2 (el primer número par)
i = 2

# Usamos un ciclo while para imprimir pares y sumarlos
while i <= n:
    print(i, end=" ")
    suma += i
    i += 2

# Imprimir la suma total
print(f", La suma es = {suma}")
