'''
Solicite o preço de uma mercadoria e o percentual de desconto.
Exiba o valor do desconto e o preço a pagar.
'''

preco = float(input("Preço da Mercadoria: "))
desconto = float(input("Porcentagem do Desconto: "))
novoPreco = preco -(preco * (desconto/100))
print ("Desconto: + R$ %.2f" % (preco * (desconto/100)))
print ("Preço a pagar: - R$ %.2f" % novoPreco)

