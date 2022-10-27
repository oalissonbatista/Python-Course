total = mais1000 = menor = cont = valor = maior = 0
while True:
    nome = input("Nome do produto: ")
    valor = float(input("preço R$"))
    continuar = input("Quer continuar? ").upper().strip()[0]
    cont += 1
    if valor > 1000:
         mais1000 += 1
    total += valor
    if cont == 1:
        valor = menor = maior
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
        
    
    if continuar == "N":
        print(f"Deu {total:.2f}")
        print(f"{mais1000}")
        print(f"{menor}")
        break
     
        
