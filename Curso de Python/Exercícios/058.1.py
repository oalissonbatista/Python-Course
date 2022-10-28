from random import randint
computador = randint(0,10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Qual o seu palpite? "))
    if computador == jogador:
        acertou = True
print("Você acertou")