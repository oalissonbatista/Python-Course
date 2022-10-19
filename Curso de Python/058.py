import random
sorteado = random.randint(0,10)
print(sorteado)
cont = 0
chute = 0
while chute != sorteado:
    chute = int(input("Digite um número de 0 a 10: "))
    if chute > sorteado:
        print('menos, tente novamente.')
    else:
        print("mais, tente novamente. ")
    if chute > 10 or chute < 0:
        print("Digite um número somente entre 0 e 10.")
    print("\033[35mVocê errou, tente novamente\033[m")
    cont += 1
print("O numero era {}, você acertou depois de {} tentativa(s).".format(sorteado,cont))