#Tabuada
num = int(input("Digite um número: "))
print("\033[33m-----TABUADA-----\033[m")
for k in range(1, 10 + 1):
    print("{} x {} = {} ".format(num,k, num*k ))
    