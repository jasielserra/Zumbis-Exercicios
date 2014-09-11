'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.


'''

valor = float(input('Valor por hora: '))
horas = int(input('Horas tralhadas: '))
bruto = valor * horas
ir = bruto * 0.11
inss = bruto * 0.08
sind = bruto * 0.05
liquido = bruto - ir - inss - sind
print ('+Salário Bruto:\t\t R$ %5.2f' %bruto)
print ('-IR:\t\t\t R$ %5.2f' %ir)
print ('-INSS:\t\t\t R$ %5.2f' %inss)
print ('-Sindicato:\t\t R$ %5.2f' %sind)
print ('=Salário Líquido:\t R$ %5.2f' %liquido)

