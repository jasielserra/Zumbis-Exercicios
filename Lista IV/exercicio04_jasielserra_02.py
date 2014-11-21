'''
Sorteie 20 inteiros entre 1 e 100 numa lista.
Armazene os números pares na lista PAR e os números ímpares na lista IMPAR.
Imprima as três listas.
'''



import random
lista = []
lista_par = []
lista_impar = []
while len(lista) < 20:
	n = random.randint(1,100)
	if n not in lista:
		lista.append(n)
	lista.sort()

for i in lista:
        if i % 2 == 0:
                lista_par.append(i)
        else:
                lista_impar.append(i)
lista_par.sort()
lista_impar.sort()
                
print('Lista:',lista)
print('Lista de Números Pares:' ,lista_par)
print('Lista de Números Ímpares:' ,lista_impar)

