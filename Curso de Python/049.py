#Tabuada
num = int(input("Tabuada do numero: "))
print("\033[33m-----TABUADA-----\033[m")
for k in range(1, 10 + 1):
    print("{} x {} = {} ".format(num,k, num*k ))
    