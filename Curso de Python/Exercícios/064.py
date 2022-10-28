#Soma de valores sem o 999
n = soma = cont = 0
while n != 999:
    n = float(input("Digite um número: "))
    soma += n 
    cont += 1
print ("Foram digitados {} números".format(cont-1))
print ("A soma entre os números digitados é = {}".format(soma-999))