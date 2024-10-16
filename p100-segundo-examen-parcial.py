# -------------------------------------------------------------
# Segundo examen Parcial                                      -
# Materia: Computacion Aplicada                               -
# Programa: Maestria en ingenieria y tecnologia aplicada      -  
# Maestro: Dr. Carlos Héctor Castañeda Ramírez                -
# Alumno: Ing. Jorge Murillo Dominguez                        -
# -------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Programa que hace lo siguente: Procesa los datos del empleado                      -
# Edad,Sexo, Sueldo y Pasatiempos                                                    - 
# Cuando ya ingresemos los suficientes datos a procesar solo intorducir " * "        -
# Al finalizar nos mostrara los datos introduciodos                                  -
# Realizara una suma de edades y un promedio de la misma                             -
# Realiazara una suma de los sueldos y un promedio de los mismos                     -
# Y finalizara diciendo cual es el mayor y el menor de los empleados introducidos    - 
# ------------------------------------------------------------------------------------
empleados = []

print("Mueblería Muebles Dico :)")
print("Sistema de Procesamiento de Empleados")
print("Captura de datos de los empleados (Pulsa * para terminar):")

# Captura de informacion de los empleados 
while True:
    nombre = input("Nombre: ")
    if nombre == "*":
        break
    edad = int(input("Edad: "))
    sexo = input("Sexo (h/m): ").lower()
    sueldo = float(input("Sueldo: "))
    pasatiempos = input("Pasatiempos (separados por comas): ").split(", ")
  

    # Agregar la informacios de los empleados a la lista de diccionarios
    empleados.append({
        "Nombre": nombre,
        "Edad": edad,
        "Sexo": sexo,
        "Pasatiempos": pasatiempos,
        "Sueldo": sueldo
    })

# Imprimir los datos almacenados en la lista de diccionarios
print("\nDatos almacenados en la lista de diccionarios:")
for empleado in empleados:
    print(empleado)

# Imprimir los datos 
print("\nTabla de datos:")
print(f"{'Nombre':<10} {'Edad':<5} {'Sexo':<5} {'Sueldo':<10} {'Pasatiempos'}")
for empleado in empleados:
    nombre = empleado['Nombre']
    edad = empleado['Edad']
    sexo = empleado['Sexo']
    sueldo = empleado['Sueldo']
    pasatiempos = ', '.join(empleado['Pasatiempos'])
    print(f"{nombre:<10} {edad:<5} {sexo:<5} {sueldo:<10.2f} {pasatiempos}")

# Procesar resumen de datos
total_empleados = len(empleados)
total_hombres = sum(1 for e in empleados if e['Sexo'] == 'h')
total_mujeres = sum(1 for e in empleados if e['Sexo'] == 'm')

# Contar los pasatiempo
pasatiempos_count = {}
for empleado in empleados:
    for pasatiempo in empleado['Pasatiempos']:
        pasatiempos_count[pasatiempo] = pasatiempos_count.get(pasatiempo, 0) + 1

# Calcular suma y promedio de edades
suma_edades = sum(e['Edad'] for e in empleados)
promedio_edades = suma_edades / total_empleados if total_empleados > 0 else 0

# Calcular suma y promedio de sueldos
suma_sueldos = sum(e['Sueldo'] for e in empleados)
promedio_sueldos = suma_sueldos / total_empleados if total_empleados > 0 else 0

# Encontrar el empleado de mayor y menor edad
# Inicializar variables con 0 para almacenar el empleado de mayor y menor edad
mayor_edad = empleados[0]
menor_edad = empleados[0]

# Aqui reccorremos la lista de los empleados para encontrar el mayor y menor de edad 
for empleado in empleados:
    if empleado['Edad'] > mayor_edad['Edad']:
        mayor_edad = empleado
    if empleado['Edad'] < menor_edad['Edad']:
        menor_edad = empleado

# Por ultimo imprimimos todos los calculos previamente realizados 

print("\nResumen:")
print(f"Empleados: {total_empleados}")
print(f"Mujeres: {total_mujeres}")
print(f"Hombres: {total_hombres}")
print("Pasatiempos:", ', '.join(f"{p}/{c}" for p, c in pasatiempos_count.items()))
print(f"Edad -> suma: {suma_edades}, Promedio: {promedio_edades:.1f}")
print(f"Sueldo -> suma: {suma_sueldos:.2f}, promedio: {promedio_sueldos:.2f}")
print(f"{mayor_edad['Nombre']} de {mayor_edad['Edad']} es el mayor, {menor_edad['Nombre']} de {menor_edad['Edad']} es el menor.")
