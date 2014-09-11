ano = int(input("Informe o Ano: "))
if ano % 4 == 0 or ano % 400 == 0:
    print("Bissexto")
else:
    print("Não é Bissexto")
