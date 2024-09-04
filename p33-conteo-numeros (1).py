import os
print("Cuenta números, los suma, cuenta positivos, negativos, ceros, para parar con -1\n")

# Inicializar las variables
c = s = 0
cp = cn = cc = 0

while True:
    num = int(input("Número? "))
    
    if num == -1:
        break
    else:
        c += 1
        s += num
        if num > 0:
            cp += 1
        elif num < 0:
            cn += 1
        else:
            cc += 1

print(f"Capturaste {c} números y su suma es {s}.")
print(f"Positivos: {cp}\nNegativos: {cn}\nCeros: {cc}")
print("\nProceso terminado.")
