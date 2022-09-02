#Somar números pares
s = 0
for k in range(0, 5+1):
    k = int(input("Digite um número: "))
    if k % 2 == 0:
        s = s + k
print ('A soma dos números pares é {}.'.format(s))