#Ano Bissexto
from datetime import date
ano = int(input(("Digite o ANO a ser analisado:")))
if ano == 0:
    ano = date.today().year
if (ano%4 == 0 and ano % 100 != 0 or ano % 400 == 0 ):
    print("{} é bissexto".format(ano))
else:
    print("{} NÃO é bissexto".format(ano))