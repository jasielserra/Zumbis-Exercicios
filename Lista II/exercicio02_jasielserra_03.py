peso = float(input("Informe peso: "))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4.00
    print(" Houve um excesso de %.2f e a multa ser paga e de R$ %.2f:" %(excesso,multa))
else:
    multa = 0
    excesso = 0
print(" Excesso de %.2f e Multa R$ %.2f" %(excesso,multa))
