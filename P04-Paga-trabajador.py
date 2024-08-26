# p044-paga-trabajador - Calcula la paga de un trabajador 

print("Calculando la paga de un trabajador :\n")

nombre = input("Dame tu nombre ?")
horas = int(input("Horas ?"))
Paga = float(input("paga x hora?" ))
tasa = 0.03

pagabruta = horas * Paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

print(f"El trabajador {nombre}, trabajo{horas} horas a una paga de{Paga}pesos,con una tasa de {tasa} ")
print(f"paga bruta: {pagabruta:,.2f}")
print(f"impuesto:{impuesto:,.2f}")

print(f"paga neta:{paganeta:,.2f}")
