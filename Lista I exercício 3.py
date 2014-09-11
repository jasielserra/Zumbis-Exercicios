'''
Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
Calcule o total em segundos.

'''


dia = int(input('Dias: '))
hora = int(input('Horas: '))
minuto = int(input('Minutos: '))
segundo = int(input('Segundos: '))

total = dia * 24 * 60 * 60 + hora * 60 * 60 + minuto * 60 + segundo
print (total)
