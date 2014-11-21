'''
Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor,
sem usar as funções max e min.
'''


import random
lista = []
while len(lista) < 10:
	n = random.randint(1,100)
	if n not in lista:
		lista.append(n)
	lista.sort()
print(lista)
print('O Maior é %d e o Menor é %d' %(lista[0],lista[9]))

