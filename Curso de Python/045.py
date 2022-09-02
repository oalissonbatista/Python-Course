from random import choice, randint
from time import sleep
itens = ['pedra','papel','tesoura']
computador = randint(0,2)
escolha = int(input("""\033[4;33;41m
-------Jokenpô--------\033[m\n
Digite [0] para PEDRA\n
Digite [1] para PAPEL\n
Digite [2] para TESOURA\n
Qual a sua jogada? """))
print("\033[35mPROCESSANDO...\033[m")
sleep(2)
print("-"*25)
print("Você jogou {}".format(itens[escolha]))
print("O computador jogou {}".format(itens[computador]))
print('-'*25)
if (computador == escolha):
    print("Não houve vencedor.")
elif computador == 0 and escolha == 1:
    print("Você ganhou!")
elif computador == 0 and escolha == 2:
    print("\033[31mVocê perdeu!\033[m")
elif computador == 1 and escolha == 2:
    print("Você ganhou!")
elif computador == 1 and escolha == 0:
    print("\033[31mVocê perdeu!\033[m")
elif computador == 2 and escolha == 0:
    print("Você ganhou!")
elif computador == 2 and escolha == 1:
    print("\033[31mVocê perdeu!\033[m")