'''
Calcule o tempo de uma viagem de carro.
Pergunte a distância a percorrer e a velocidade
média esperada para a viagem.
'''

distancia = float(input("Distância em Km: "))
velocidade = float(input("Velocidade média em km/h:"))
tempo = distancia/velocidade
print("Tempo da viagem é de aproximadamente %.1f horas:" % tempo)
