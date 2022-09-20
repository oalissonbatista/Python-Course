from datetime import date
ma = 0
me = 0
for k in range (1,7+1):
    ano = int(input("Qual seu ano de nascimento? "))
    idade = (date.today().year - ano)
    if idade >= 18:
        ma = k
    elif idade < 18:
        me = k - ma
print("{} são maiores de idade e {} não são.".format(ma,me))