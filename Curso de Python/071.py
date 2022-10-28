valor = int(input("Digite o valor a ser sacado: "))
total = valor
print("O caixa possui cédulas de R$50,00 R$20,00 R$10,00 e R$1,00")
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced +=1
    else:
        if totalced > 0:
            print(f"total de {totalced} cédulas de {ced}")
        if ced == 50:
            ced ==20
        if ced == 20:
            ced == 10
        if ced == 10:
            ced == 1
        totalced =0
        if total == 0:
            break
print("Volte sempre.")
        
            
