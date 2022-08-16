#Ano Bissexto
ano = int(input(("Digite o ANO:")))
if (ano%4) == 0:
    print("{} é bissexto".format(ano))
else:
    print("{} NÃO é bissexto".format(ano))