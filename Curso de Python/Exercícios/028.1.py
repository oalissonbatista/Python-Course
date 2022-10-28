#Adivinhando número
from random import randint
from time import sleep
computador = randint(0,5)
print("-"*52)
print("Vou pensar em um número de 0 a 5. Tente adivinhar...")
print("-"*52)
chute = int(input("Chute um número:"))
print("PROCESSANDO...")
sleep(3)
if chute == computador:
    print("Parabéns, você acertou")
else:
    print("Você errou, o número era: {}".format(computador))