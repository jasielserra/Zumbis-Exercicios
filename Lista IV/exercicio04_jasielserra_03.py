'''
Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100.
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
intercalados dos dois outros vetores.Imprima os três vetores.

'''



import random
vetor1 = []
vetor2 = []
vetor3 = []
while len(vetor1) < 10:
	n = random.randint(1,100)
	vetor1.append(n)

while len(vetor2) < 10:
	n = random.randint(1,100)
	vetor2.append(n)
i = 0
while len(vetor3) < 20:
        vetor3.append(
   
      

                
print('Lista de Números 1:',vetor1)
print('Lista de Números 2:' ,vetor2)
print('Lista de Números 3:' ,vetor3)

