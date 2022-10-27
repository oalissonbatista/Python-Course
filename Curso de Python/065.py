n = 0
x = 0
soma = 0
maior = 0
menor = 0
cont = 0
while x != "N":
    n = float(input("Digite um número: "))
    soma += n 
    cont +=1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    x = input("\033[31mDeseja continuar? \033[m").upper().strip()[0]
media = soma / cont
print("FIM")
print ("Você digitou {} números e média foi {:.2f} ".format(cont,media))
print ("O maior valor digitado foi {}".format(maior))
print("O menor valor digitado foi {}".format(menor))
