n = int(input("Digite um número: "))
mult = 0
for k in range (2,n):
    if n % k == 0:
        print("É multiplo de {}".format(k))
        mult +=1
if mult == 0:
    print("\033[31mÉ um número primo!\033[m")
else:
    print("\033[31mNão é primo!\033[m")