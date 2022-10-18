n = 0
soma = 0
cont = 0
while n != 999:
    n = float(input("Digite um número: "))
    soma += n 
    cont += 1

print ("Foram digitados {} números".format(cont))
print ("A soma entre os números digitados é = {}".format(soma-999))