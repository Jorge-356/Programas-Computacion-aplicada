# Calcular cantidad de productos y subtotal por cliente
import os
os.system('cls')

# Introducir datos de compras
n = int(input("Número de compras: "))
compras = []

# Bucle para recopilar la información de cada compra
for i in range(1, n + 1):
    print(f'\n------ Compra {i} ------')
    compra = {
        "cliente": input("Nombre Cliente: "),
        "producto": input("Nombre Producto: "),
        "cantidad": int(input("Cantidad: ")),
        "precio": float(input("Precio: "))
    }
    compras.append(compra)

print('\nDiccionario de compras:\n', compras)

# Calcular cantidad de productos y subtotal por cliente
clientes = {}

for compra in compras:
    cliente = compra["cliente"]
    if cliente not in clientes:
        clientes[cliente] = {"cantidad": 0, "subtotal": 0}

    clientes[cliente]["cantidad"] += compra["cantidad"]
    clientes[cliente]["subtotal"] += compra["cantidad"] * compra["precio"]

# Imprime los clientes y sus subtotales
print('\nLos clientes y sus totales\n')
for cliente, datos in clientes.items():
    print(f"Cliente : {cliente}")
    print(f"Cantidad : {datos['cantidad']}")
    print(f"Subtotal : {datos['subtotal']:.2f}")
    print()

print('\nDiccionario de clientes:\n', clientes)
