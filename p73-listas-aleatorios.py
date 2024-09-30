# Listas con aleatorios
import random, os
os.system('clear')

l1 = []
l2 = []
l3 = []

print("Generando aleatorios ...")

# Generando números aleatorios para las listas
for n in range(10):
    l1.append(random.randint(1, 100))
    l2.append(random.randint(1, 100))

print("\nListas originales:")
print(f"Lista 1: {l1}")
print(f"Lista 2: {l2}")

# Procesando las listas (elevando al cuadrado los elementos y sumándolos en l3)
for n in range(10):
    l1[n] = pow(l1[n], 2)
    l2[n] = pow(l2[n], 2)
    l3.append(l1[n] + l2[n])

print("\nListas procesadas:")
print(f"Lista 1 (al cuadrado): {l1}")
print(f"Lista 2 (al cuadrado): {l2}")
print(f"Lista 3 (suma de las dos listas): {l3}")
