# Indica cual es el mayor de tres numeros 
print("Dame 3 numeros para saber cual es el mayor de los 3 ")
n1, n2, n3 = map(int, input().split())
if n1>n2 and n1>n3:
    print(f"\nEl numero {n1} es el mayor\n")
elif n2>n1 and n2>n3:   
     print(f"\nEl numero {n2} es el mayor\n")
else:
     print(f"\nEl numero {n3} es el mayor\n")
