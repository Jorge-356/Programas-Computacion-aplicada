# Procesar pizza
import os
os.system('cls')

# Diccionario de ingredientes y sus precios
ingr = {'T': 1.50, 'P': 3.50, 'C': 3.74, 'A': 0.40}
base = 15  # Precio base de la pizza
st = 0  # Subtotal inicial
tot = 0  # Total inicial

# Solicitar al usuario los ingredientes
pedido = input('Ingredientes de tu pizza? ').upper()

# Calcular el subtotal sumando los precios de los ingredientes seleccionados
for i in pedido:
    if i in 'TPCA':
        st += ingr[i]

# Añadir el precio base al subtotal
st += base

# Calcular el total con descuento si el subtotal es mayor o igual a 20
if st >= 20:
    tot = st - (st * 0.05)  # Aplicar un 5% de descuento
else:
    tot = st  # Si no hay descuento, el total es igual al subtotal

# Mostrar el subtotal y el total
print(f'El subtotal es: {st}')
print(f'El total es: {tot}')
