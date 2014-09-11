n1 = int(input("Informe um numero: "))
n2 = int(input("Informe outro numero: "))
n3 = int(input("Informe outro numero: "))

if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n3 and n2 >= n1:
    maior = n2
else:
    maior = n3
print(" Número maior é %d: " %maior)
