n = 0
x = 0
soma = 0
maior = n
menor = n
while x != 'NAO':
    n = float(input("Digite um número: "))
    x = input("\033[31mDeseja continuar? \033[m").upper()
    soma += n 
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print (soma)
print (maior)
print(menor)
