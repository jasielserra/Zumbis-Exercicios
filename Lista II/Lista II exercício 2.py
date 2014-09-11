'''
   Faça um Programa que peça um número correspondente a um determinado ano e
   em seguida informe se este ano é ou não bissexto.

'''


a = int(input('Ano: '))
if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
  print ('Bissexto')
else:
  print ('Não é bissexto')
