s = 0
cont = 0
inicio = int(input("Digite o inicio do intervalo: "))
fim = int(input("digite o final do intervalo: "))
for k in range (inicio, fim + 1):
    if k % 2 != 0 and k % 3 == 0:
        cont += 1 
        s += k
print("A Soma é de {} valores".format(cont))
print ("A soma entre os números ímpares e múltiplos de 3 no intervalo de {} até {} é = {}".format(inicio, fim,s))