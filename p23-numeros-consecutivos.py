# Dado tres numeros indica si son o no consecutivos 
print("Dame 3 numeros para saber si son consecutivos2 ")
n1, n2, n3 = map(int, input().split())
if n2 - n1 == 1 and n3 - n2 == 1:
    print("\nSi son numeros consecutivos\n")
  
else:
    print("\nNo son numeros consecutivos\n")    

