''''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.Faça um programa que calcule e escreva o número
de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de
crescimento
'''

a = 80000
b = 200000
anos = 0
while True:
    tx_a = a * (3/100)
    tx_b = b * (1.50/100)
    b = b + tx_b #Acumulador
    a = a + tx_a #Acumulador
    anos +=1     #Contador
    if a >= b:
        break
print('Serão necessários %d anos para que o país A ultrapasse B' % anos)
