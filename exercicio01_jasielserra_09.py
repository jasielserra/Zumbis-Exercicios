'''
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
'''

qtd_km = float(input('Km rodado: '))
qtd_dias = float(input('Dias: '))
preco = qtd_km * 0.15 + qtd_dias * 60.00
print('Preço a Pagar - R$ %.2f ' % preco)
