# Nombres y edades
import os
os.system('cls')

print('Nombres y edades\n')
print("Introduce los nombres y edades: * en nombre termina\n")

nombres = []
edades = []

# Lectura de nombres y edades
while True:
    nombre = input("Nombre: ")
    if nombre == "*":
        break
    else:
        nombres.append(nombre)
        edad = int(input("Edad: "))
        edades.append(edad)

# Imprimir alumnos mayores de edad
print("\nAlumnos mayores de edad:")
for i in range(len(nombres)):
    if edades[i] >= 18:
        print(f"Nombre: {nombres[i]}, Edad: {edades[i]}")

# Encontrar e imprimir el alumno de mayor edad
pos = edades.index(max(edades))
print(f"\nAlumno de mayor edad: {nombres[pos]}, {edades[pos]}")
