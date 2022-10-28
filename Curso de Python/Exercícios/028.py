#adivinhando numero
import random
n = [0,1,2,3,4,5]
escolhido = random.choice(n)
chute = int(input("Qual número foi escolhido?"))
if chute == escolhido:
    print("YOU WIN")
    print("O número era {}".format(escolhido))
else:
    print("YOU LOSE")
    print("o numéro era {}".format(escolhido))