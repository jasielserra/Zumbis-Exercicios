'''
Faça um programa que calcule o aumento de um salário.
Ele deve solicitar o valor do salário e a porcentagem do aumento.
Exiba o valor do aumento e do novo salário.
'''

salario = float(input("Salario: "))
aumento = float(input("Porcentagem do Aumento: "))
novoSalario = salario +(salario * (aumento/100))
print ("Novo salario: R$ %.2f" % novoSalario)
print ("Aumento: R$ %.2f" % (salario * (aumento/100)))
