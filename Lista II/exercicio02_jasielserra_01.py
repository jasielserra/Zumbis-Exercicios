lado1 = int(input("Informe um lado do triangulo"))
lado2 = int(input("Informe outro lado do triangulo"))
lado3 = int(input("Informe o ultimo lado do triangulo"))

if lado3 > lado1 + lado2 or lado1 > lado2 + lado3  or lado2 > lado3 + lado1 :
print("Não é um triangulo")
print("A Soma dos lados é maior que soma do terceiro")

elif lado1 == lado2 == lado3:
    print("Triângulo Equilátero")
elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
    print("Triângulo Isósceles")
else:
    print("Triângulo Escaleno")
    
