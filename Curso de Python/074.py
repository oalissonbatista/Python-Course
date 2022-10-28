from random import randint
n = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
maior = 0
menor = 10
if n[0] > maior:
    maior = n[0]
elif n[0] < menor:
    menor = n[0]
if n[1] > maior:
    maior = n[1]
elif n[1] < menor:
    menor = n[1]
if n [2] > maior:
    maior = n[2]
elif n[2] < menor:
    menor = n[2]
if n[3] > maior:
    maior = n[3]
elif n [3] < menor:
    menor = n[3]
if n[4] > maior:
    maior = n[4]
elif n[4] < menor:
    menor = n[4]
print(f"Os números sorteados foram: {n}")
print(f"O maior é {maior}")
print(f'O menor é {menor}')

