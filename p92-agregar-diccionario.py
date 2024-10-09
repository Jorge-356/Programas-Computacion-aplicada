# Creación del diccionario con las ventas
ventas = {
    "Juan": 1550,
    "Jose": 2600,
    "Maria": 2220
}

# Mostrar el diccionario inicial
print("Diccionario inicial:", ventas)

# Agregar elementos al diccionario usando []
ventas["Rocio"] = 2500
ventas["Mateo"] = 1567

# Agregar elementos al diccionario usando update()
ventas.update({"Andrea": 9567})
ventas.update({"Miguel": 1234})

# Mostrar el diccionario modificado
print("Diccionario modificado:", ventas)
