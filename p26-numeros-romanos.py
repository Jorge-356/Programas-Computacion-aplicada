# Programa que transforma en numero romano del 1 al 10 
# Entrada del usuario
numero = int(input("Ingresa un número entre 1 y 10: "))

def NN(numero):
    dias = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X",
    }
    
    # Verificamos si el número está en el rango válido
    if numero in dias:
        return dias[numero]
    else:
        return "Numero inválido"



# Llamada a la función y salida del resultado
print(NN(numero))
