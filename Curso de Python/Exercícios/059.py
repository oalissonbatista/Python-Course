n1 = float(input ("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
print("""
--------Menu--------
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa """)
escolha = 0
while escolha != 5:
    escolha = int(input("Digite a opçao desejada: "))
    if escolha == 1:
        print("\033[34mSoma: {} + {} = {}\033[m".format(n1,n2, n1+n2))
    elif escolha == 2:
        print("\033[31mMultiplicação: {} X {} = {}\033[m".format(n1,n2,n1*n2))
    elif escolha == 3:
        if n1 > n2:
            print("\033[33m{} é maior que {}\033[m".format(n1,n2))
        elif n1 == n2:
            print("O números são iguais")
        else:
            print("\033[32m{} é maior que {}\033m".format(n2,n1))
    elif escolha == 4:
        print("\033[35mEscolha novamente: \033[m")
        n1 = float(input ("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print("""--------Menu--------
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa """)
    else:
        print("\033[31mOpção inválida, tente novamente.\033[m")

print("VOCÊ SAIU!")
