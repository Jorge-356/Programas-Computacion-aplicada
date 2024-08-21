# Calcular el area de un triangulo 

print("Calculando el area de un triangulo")
print("Dame la base y la altura separados por un enter")
base,altura = int(input()), int(input())

area = (base * altura) /2
print (f"Para un triangulo de base {base} y altura el area es {area:.2f}")