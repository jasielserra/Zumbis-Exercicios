'''
Escreva um programa para calcular a redução do tempo de vida de um fumante.
Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá.
Exiba o total de dias.

'''
qtd_cigarros = int(input("Quantos cigarros fuma por dia? "))
qtd_anos = int(input('Fuma a Quantos anos ?'))
cigarro_fumados = (qtd_cigarros * 365 * qtd_anos)

