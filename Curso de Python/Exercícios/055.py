maior = 0
menor = 0
for k in range (1, 5+1):
    peso = float(input("Digite o peso:"))
    if k ==1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("Maior peso: {:.2f}". format(maior))
print("Menor peso: {:.2f}".format(menor))