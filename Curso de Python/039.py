from datetime import date
ano = int(input("Qual o seu ano de nascimento?"))
idade = ((date.today().year) - ano)

if idade > 18:
    print("\033[31mEra pra você ter se alistado {} anos atrás.\033[m".format((idade-18)))
elif idade < 18:
    print("\033[31mFaltam {} anos para você se alistar.\033[m".format(18-idade))
else:
    print("\033[31mEsse ano você completa 18, está na hora de se alistar!\033[m")
