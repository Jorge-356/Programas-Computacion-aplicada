# Simulación de un sistema de ventas para una tienda

class Transaccion:
    def __init__(self, producto, unidades, precio_unitario):
        self.producto = producto
        self.unidades = unidades
        self.precio_unitario = precio_unitario
        self.monto_total = unidades * precio_unitario

    def __str__(self):
        return f"Producto: {self.producto:<15} Cantidad: {self.unidades:>10,.2f} Total: {self.monto_total:>10,.2f}"

class Comprador:
    def __init__(self, identificador, nombre, direccion, email):
        self.identificador = identificador
        self.nombre = nombre
        self.direccion = direccion
        self.email = email
        self.transacciones = []

    def agregarTransaccion(self, transaccion):
        self.transacciones.append(transaccion)

    def calcularTotal(self):
        total = sum(transaccion.monto_total for transaccion in self.transacciones)
        return total

    def __str__(self):
        return (f"Comprador [Nombre = {self.nombre:<20} ID: {self.identificador:<12} "
                f"Dirección: {self.direccion:<20} Email: {self.email:<20}] - "
                f"Total Compras: {self.calcularTotal():,.2f}")

class Establecimiento:
    def __init__(self, nombre, direccion, dueño):
        self.nombre = nombre
        self.direccion = direccion
        self.dueño = dueño
        self.lista_compradores = []

    def registrarComprador(self, comprador):
        self.lista_compradores.append(comprador)

    def contarVentas(self):
        total_ventas = sum(len(comprador.transacciones) for comprador in self.lista_compradores)
        return total_ventas

    def calcularVentasTotales(self):
        total_importe = sum(comprador.calcularTotal() for comprador in self.lista_compradores)
        return total_importe

    def __str__(self):
        return (f"Establecimiento [Nombre: {self.nombre} Dirección: {self.direccion} "
                f"Propietario: {self.dueño}] - Total Ingreso: {self.calcularVentasTotales():,.2f}")

def registrarComprador():
    print("Ingrese la información del comprador:")
    identificador = input("ID: ")
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    email = input("Email: ")
    comprador = Comprador(identificador, nombre, direccion, email)
    return comprador

def agregarTransacciones(comprador):
    print(f"Captura de transacciones para {comprador.nombre}")
    while True:
        producto = input("Producto: ")
        if producto == "":
            break
        unidades = int(input("Cantidad: "))
        precio_unitario = float(input("Precio Unitario: "))
        comprador.agregarTransaccion(Transaccion(producto, unidades, precio_unitario))

def main():
    import os
    os.system("cls")

    # Creación de la tienda con clientes y transacciones iniciales
    mi_establecimiento = Establecimiento("Tienda los Pinos", "Av Central 123", "José Martínez")

    mi_establecimiento.registrarComprador(Comprador("ABC123456", "Luis Perez", "Calle Arce 120", "luis@gmail.com"))
    mi_establecimiento.lista_compradores[0].agregarTransaccion(Transaccion("Destornillador", 5, 150))
    mi_establecimiento.lista_compradores[0].agregarTransaccion(Transaccion("Martillo", 2, 320))

    mi_establecimiento.registrarComprador(Comprador("DEF789101", "Ana Lopez", "Calle Pino 23", "ana@gmail.com"))
    mi_establecimiento.lista_compradores[1].agregarTransaccion(Transaccion("Clavos", 50, 8))
    mi_establecimiento.lista_compradores[1].agregarTransaccion(Transaccion("Pintura", 3, 200))

    # Registrar un nuevo comprador y sus transacciones
    nuevo_comprador = registrarComprador()
    agregarTransacciones(nuevo_comprador)
    mi_establecimiento.registrarComprador(nuevo_comprador)

    # Generar un reporte final
    print("\nReporte de Ventas:", mi_establecimiento)
    print("Total de Compradores:", len(mi_establecimiento.lista_compradores))
    print("Ventas Totales:", mi_establecimiento.contarVentas())

    print("\nListado de Compradores:")
    for comprador in mi_establecimiento.lista_compradores:
        print(comprador)
        for transaccion in comprador.transacciones:
            print(transaccion)
        print()

if __name__ == "__main__":
    main()
