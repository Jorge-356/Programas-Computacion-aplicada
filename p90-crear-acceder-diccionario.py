# Creación del diccionario con llaves nuemericas con los días de la semana
dias = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}

# Mostrar el diccionario completo
print("Diccionario completo:", dias)

# Acceder y mostrar el primer elemento usando []
print("Primer elemento usando []:", dias[1])

# Acceder y mostrar el último elemento usando []
print("Último elemento usando []:", dias[7])

# Acceder y mostrar el quinto elemento usando get()
print("Quinto elemento usando get():", dias.get(5))

# Acceder y mostrar el séptimo elemento usando get()
print("Séptimo elemento usando get():", dias.get(7))

# Mostrar nuevamente el diccionario completo
print("Diccionario completo:", dias)
