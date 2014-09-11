'''
Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
Calcule o total em segundos.

'''



dia = int(input("Dia: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos:"))
dia = dia * 24 * 60 * 60     # Converta Dias em segundos
horas = horas * 60 * 60      # Converta Horas em segundos
minutos = minutos * 60       # Converta minutos em segundos
total = dia + horas + minutos + segundos # Some tudo
print("Voce tem %d segundos " % total)
