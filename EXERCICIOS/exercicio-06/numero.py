n1 = int (input ("digite numero 1:"))
n2 = int (input ("digite numero 2:"))
n3 = int (input ("digite numero 3:"))
if n1 > n2 and n3:
    print (f" o {n1} é maior")
elif n2 > n1 and  n2 > n3 :
    print (f" o {n2} e maior")
else:
    print(f"o {n3 } e maior")