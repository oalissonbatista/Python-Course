from datetime import date
ano = int(input("Digite o ano de nascimento do atleta: "))
idade = ((date.today().year) - ano)
print("Você tem {} anos".format(idade))
if idade <= 9:
    print("Você é da categoria MIRIM")
elif idade <= 14:
    print("Você é da categoria INFANTIL")
elif idade <= 19:
    print("Você é da categoria JUNIOR")
elif idade <= 25:
    print("Você é da categoria SÊNIOR")
else:
    print("Você é da categoria ADULTO")