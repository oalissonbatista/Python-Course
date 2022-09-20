s = 0
inicio = int(input("Digite o inicio do intervalo: "))
fim = int(input("digite o final do intervalo: "))
for k in range (inicio, fim + 1):
    if k % 2 != 0 and k % 3 == 0:
        s += k
print ("A soma ente os números ímpares e múltiplos de 3 no intervalo de {} até {} é = {}".format(inicio, fim,s))