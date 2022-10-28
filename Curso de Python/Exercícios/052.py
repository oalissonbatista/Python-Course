n = int(input("Digite um número: "))
cont = 0
for k in range (1,n +1):
    if n % k == 0:
        print("É multiplo de {}".format(k))
        cont += 1
if cont == 2:
    print("\033[31mÉ um número primo!\033[m")
else:
    print("\033[31mNão é primo!\033[m")