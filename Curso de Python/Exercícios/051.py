inicio = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))
decimo = inicio + (10-1)  * r
for k in range (inicio,decimo + r,r):
    print(k, end= " ")