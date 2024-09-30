# Procesar una lista de calificaciones introducida por el usuario 
import os
os.system('cls')

print('Procesar calificaciones \n')
print("Introduce calificaciones entre 0 y 10 (99 para terminar):\n")

nums = []
n = suma = prom = 0

while n != 99:
    n = float(input("Número > "))
    if n >= 0 and n <= 10:
        nums.append(n)
        suma += n
    elif n != 99:
        print('Calificación inválida, ingresa un número entre 0 y 10.')

if len(nums) > 0:
    prom = suma / len(nums)
else:
    prom = 0

mp = []
for n in nums:
    if n > prom:
        mp.append(n)

print(f"\nCapturaste {len(nums)} números")
print(f"Los números son: {nums}")
print("\nEstadísticas >>")
print(f"Suma: {suma}")
print(f"Promedio: {prom:.2f}")
print(f"Mayores al promedio: {len(mp)} : {mp}")
print(f"Mayor: {max(nums)}")
print(f"Menor: {min(nums)}")
