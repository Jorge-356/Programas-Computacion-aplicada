# Creación del diccionario con llaves con los países y sus valores
paises = {
    "Argentina": 100,
    "Brasil": 200,
    "Colombia": 300,
    "Chile": 400,
    "Ecuador": 500,
    "Bolivia": 600,
    "Jamaica": 700
}

# Mostrar el diccionario inicial
print("Diccionario inicial:", paises)

# Modificar el valor de la llave 'Brasil' a 250 usando []
paises["Brasil"] = 250

# Modificar el valor de la llave 'Chile' a 450 usando []
paises["Chile"] = 450

# Modificar el valor de la llave 'Bolivia' a 650 usando update()
paises.update({"Bolivia": 650})

# Modificar el valor de la llave 'Jamaica' a 750 usando update()
paises.update({"Jamaica": 750})

# Mostrar el diccionario modificado
print("Diccionario modificado:", paises)
