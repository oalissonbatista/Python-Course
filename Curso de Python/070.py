total = mais1000 = menor = cont = valor = maior = 0
barato = ' '
while True:
    nome = input("Nome do produto: ")
    valor = float(input("preço R$"))
    continuar = " "
    while continuar not in 'SN':
        continuar = str(input("Quer continuar? ")).upper().strip()[0]
    cont += 1
    if valor > 1000:
         mais1000 += 1
    total += valor
    if cont == 1:
        menor = valor 
    else:
        if valor < menor:
            menor = valor
            barato = nome
    if continuar == "N":
        print(f"total = R${total:.2f}")
        if mais1000 == 0:
            print("Nenhum dos produtos custa mais de R$1000,00.")
        else:
            print(f"{mais1000} produtos custam mais de R$1000,00.")
        print(f"O produto mais barato foi o(a){barato}.")
        break
     
        
