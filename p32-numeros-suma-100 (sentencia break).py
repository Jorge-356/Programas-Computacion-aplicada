
print("\nImprime")

c= 0
s = 0

while c < 300:
    c= c +1
    s= s + c
    print(c, end ="")
    if s >=10000:
        print("\n")
        break

print(f"\nLa suma es {s}, simando {c} numeros")    