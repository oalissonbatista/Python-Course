n = int(input("Digite um número: "))
x = n
fatorial = 1
while x > 0:
    fatorial = fatorial * x
    x -= 1
print("O fatorial de {} é {}".format(n,fatorial))