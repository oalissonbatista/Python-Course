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
        print("{} + {} = {}".format(n1,n2, n1+n2))
    if escolha == 2:
        print("{} X {} = {}".format(n1,n2,n1*n2))
    if escolha == 4:
        print("Escolha novamente: ")
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
