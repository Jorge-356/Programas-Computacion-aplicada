# Definimos una función para convertir un número en el día de la semana correspondiente
def dia_semana(numero):
    dias = {
        1: "Domingo",
        2: "Lunes",
        3: "Martes",
        4: "Miércoles",
        5: "Jueves",
        6: "Viernes",
        7: "Sábado"
    }
    
    # Verificamos si el número está en el rango válido
    if numero in dias:
        return dias[numero]
    else:
        return "Día inválido"

# Entrada del usuario
numero = int(input("Ingresa un número entre 1 y 7: "))

# Llamada a la función y salida del resultado
print(dia_semana(numero))
