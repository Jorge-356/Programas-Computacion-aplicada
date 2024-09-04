# Programa que baja numeros hasta donde se lo indiques de 2 en 2
n = int(input("Ingresa el número hasta el cual deseas imprimir: "))

i = 100
while i >= n:
    print(i)
    i -= 2
