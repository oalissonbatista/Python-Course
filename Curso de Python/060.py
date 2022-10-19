#fatorial por for
n = int(input("Digite um número: "))
cont = 1
for fat in range(1,n+1):
    cont *= fat
print("\033[31m{}! = {}\033[m".format(n,cont))
