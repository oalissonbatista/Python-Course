from random import choice
from time import sleep

pedra = 1
papel = 2
tesoura = 3
escolha = int(input("\033[4;33;41m-------Jokenpô--------\033[m\nDigite 1 para PEDRA\nDigite 2 para PAPEL\nDigite 3 para TESOURA\n"))
comp = [pedra,papel,tesoura]
pc = choice(comp)
print("pc == {}".format(pc))
print("\033[35mPROCESSANDO...\033[m")
sleep(2)
if (pc == escolha):
    print("Não houve vencedor.")
elif pc == pedra and escolha == 2:
    print("Você ganhou!")
elif pc == pedra and escolha == 3:
    print("\033[31mVocê perdeu!\033[m")
elif pc == papel and escolha == 3:
    print("Você ganhou!")
elif pc == papel and escolha == 1:
    print("\033[31mVocê perdeu!\033[m")
elif pc == tesoura and escolha == 1:
    print("Você ganhou!")
elif pc == tesoura and escolha ==2:
    print("\033[31mVocê perdeu!\033[m")