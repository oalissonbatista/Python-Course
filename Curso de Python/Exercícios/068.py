from random import randint
from time import sleep
cont = pc = 0
while True:
    print("-"*5 + "Jogo PAR OU ÍMPAR" + "-"*5)
    n = int(input("Digite um número: "))
    impar_par = " "
    while impar_par not in "PI":
        impar_par = str(input("PAR OU ÍMPAR? ")).upper().strip()[0]
    pc = randint(0,10)
    soma = n + pc
   
    if (soma % 2 == 0 and impar_par == 'P') or (soma % 2 != 0 and impar_par == 'I') :
        print("-"*20)
        print(f"Você jogou {n} e o computador jogou {pc}.", end ='')
        print("DEU PAR" if soma % 2 == 0 else "DEU ÍMPAR")
        sleep(1)
        print("-"*20)
        print("\033[34mVocê venceu!\033[m")
        print("-"*20)
        sleep(1)
        print("\033[31mVamos jogar novamente...\033[m")
        cont +=1
    else:
        print(f"Você jogou {n} e o computador jogou {pc}.")
        print(f"GAME OVER! Você venceu {cont} vez(es)")
        break
