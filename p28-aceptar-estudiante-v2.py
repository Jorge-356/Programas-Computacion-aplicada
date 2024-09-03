# Función para determinar si un estudiante es aceptado
# Entrada de datos
nombre = input("Introduce el nombre del estudiante: ")
sexo = input("Introduce el sexo del estudiante (H/M): ")
edad = int(input("Introduce la edad del estudiante: "))
calificaciones = list(map(int, input("Introduce las tres calificaciones separadas por espacio: ").split()))
def evaluar_estudiante(nombre, sexo, edad, calificaciones):
    promedio = sum(calificaciones) / len(calificaciones)
    
    if sexo.lower() != 'm':
        return f"{nombre}, solo aceptamos mujeres."
    elif edad <= 21:
        return f"{nombre}, eres mujer, pero no tienes la edad, solo mayores a 21."
    elif promedio < 8 or promedio > 9.5:
        return f"{nombre}, eres mujer, tienes la edad, pero tu promedio no alcanza, solo promedios de 8 a 9.5."
    else:
        return f"{nombre}, has sido aceptada, tu edad de {edad} y tus calificaciones {calificaciones}, lo permiten."


# Evaluación y resultado
resultado = evaluar_estudiante(nombre, sexo, edad, calificaciones)
print(resultado)
