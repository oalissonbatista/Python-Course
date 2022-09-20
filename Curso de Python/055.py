s = 0
for k in range (1, 5+1):
    peso = float(input("Digite o peso:"))
    if peso+k > peso:
        s += k
        print(s)