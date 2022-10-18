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
        print("Soma: {} + {} = {}".format(n1,n2, n1+n2))
    if escolha == 2:
        print("Multiplicação: {} X {} = {}".format(n1,n2,n1*n2))
    if escolha == 3:
        if n1 > n2:
            print("{} é maior que {}".format(n1,n2))
        elif n1 == n2:
            print("O números são iguais")
        else:
            print("{} é maior que {}".format(n2,n1))
    if escolha == 4:
        print("\033[35mEscolha novamente: \033[m")
        n1 = float(input ("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print("""
--------Menu--------
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa """)

print("Você saiu")
