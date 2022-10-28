nota1 = float(input("Qual a nota 1?"))
nota2 = float(input("Qual a nota 2?"))
media = ((nota1 + nota2) /2)
print("A média foi {}".format(media))
if media < 5:
    print("\033[31mVocê foi REPROVADO!\033[m")
elif media > 5 and media < 7:
    print("\033[31mVocê está de RECUPERAÇÃO!\033[m")
elif media == 10:
    print("PARABÉNS, você teve 100% de aproveitamento.")
elif media > 7:
    print("\033[34mPARABÉNS!!! Você foi APROVADO.\033[m")
