from datetime import date
ma = 0
me = 0
for k in range (1,7+1):
    ano = int(input("Qual seu ano de nascimento? "))
    idade = (date.today().year - ano)
    if idade >= 18:
        ma += 1
    elif idade < 18:
        me +=1
if me == 0:
    print("Todos são maiores de idade")
elif ma == 0:
    print("Todos são menores de idade")
else:
    print("{} são maiores de idade e {} não são.".format(ma,me))