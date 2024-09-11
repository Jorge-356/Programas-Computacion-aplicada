# Primer examen parcial 
# Programa que realiza lo siguente: 
# Tipo de usuario: [1] Alumno $100, [2] Trabajador $200, [3] Docente $500
# Tipo de paquete: [1] Solo conferencias $600, [2] Con eventos sociales $800, [3] Con kit de acceso $900
# Se debe calcular un subtotal de la venta sumando el precio del tipo de usuario más el precio de tipo de paquete,
# y multiplicando por la cantidad solicitada.
# Se otrgará un descuento siempre y cuando el subtotal sea mayor a 5,000 y de acuerdo a lo siguiente
# • Es Alumno 20%
# • Es Trabajador y un 10%
# • Es Docente y un 5%
# Al final mostrar un resumen con los datos calculados de la venta.
# Al terminar de procesar las ventas mostrar el total de ventas del día:
# Materia: Computacion Aplicada 
# Alumno: Ing. Jorge Murillo Dominguez 
# Docente: Dr. Carlos Castañeda 


print('Universidad Autonoma De Zacateca')
print('---Evento academico Pitec---')
print('Sistema de inscripción Congreso de Sistemas')


Venta_Final = 0 # Se inicia esta variable a 0 
Opciones = 'Chivas_Rayadas_Del_Guadalajara'
 # Menu
while Opciones == 'Chivas_Rayadas_Del_Guadalajara':
    print("Tipo de usuario:")
    print("[1] Alumno $100")
    print("[2] Trabajador $200")
    print("[3] Docente $500")
    tipo_usuario = int(input())
    
    if tipo_usuario == 1:
        costo_usuario = 100
    elif tipo_usuario == 2:
        costo_usuario = 200
    elif tipo_usuario == 3:
        costo_usuario = 500
    else:
        print("Solo tengo programado 3 tipos de usuarios")
        continue

    print("Tipo de paquete:")
    print("[1] Solo conferencias $600")
    print("[2] Con eventos sociales $800")
    print("[3] Con kit de acceso $900")
    tipo_paquete = int(input("Elige el tipo de paquete (1, 2, 3): "))

 # Aqui se define el costo segun el paquete elegido 
    if tipo_paquete == 1:
        costo_paquete = 600
    elif tipo_paquete == 2:
        costo_paquete = 800
    elif tipo_paquete == 3:
        costo_paquete = 900
    else:
        print("Solo tengo programado 3 tipos de paquetes")
        continue

    cantidad = int(input("Introduce la cantidad de inscripciones: "))

    # Aqui se calcula el subtotal 
    subtotal = (costo_usuario + costo_paquete) * cantidad

    # Calcular el descuento
    descuento = 0
    if subtotal > 5000:
        if tipo_usuario == 1:
            descuento = subtotal * 0.20  # Alumno 20%
        elif tipo_usuario == 2:
            descuento = subtotal * 0.10  # Trabajador 10%
        elif tipo_usuario == 3:
            descuento = subtotal * 0.05  # Docente 5%

    # Calcular el total después del descuento
    total = subtotal - descuento

   
    print("\nResumen de la venta:")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento: ${descuento:.2f}")
    print(f"Total a pagar: ${total:.2f}\n")

    # Acumular el total si es que hat mas de una transaccion 
    Venta_Final = Venta_Final + total

    continuar = input("¿Deseas continuar? (s/n): ").lower()
print(f"\nImporte total de la Venta: ${Venta_Final:.2f}")

