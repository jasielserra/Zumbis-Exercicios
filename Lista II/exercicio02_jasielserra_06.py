sal_horas = float(input("Salario por horas: "))
horas = int(input("Horas trabalhadas no mês:" ))
sal_bruto = sal_horas * horas
inss = sal_bruto * (8/100)
sind = sal_bruto * (5/100)
irpf = sal_bruto * (11/100)
sal_liquido = sal_bruto - inss - sind - irpf
print(" + Salario Bruto + R$ %.2f :" %sal_bruto)
print(" - IRPF - R$ %.2f :" %irpf)
print(" - INSS - R$ %.2f :" %inss)
print(" - Sindicato - R$ %.2f :" %sind)
print(" = Salario Liquido = R$ %.2f :" %sal_liquido)
