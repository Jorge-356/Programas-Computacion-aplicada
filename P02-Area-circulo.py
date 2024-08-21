#p02-area-circulo- calcula el area de un circulo

import math

print("Calculamos el area de un circulo : \n")
radio = float (input ("Dame el radio ?"))

area = math.pi * radio ** 2 

print(f"\nPara un circulo de radio {radio} el area es {area:2f}")