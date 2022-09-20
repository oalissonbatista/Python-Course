print("Digite o intervalo para separação dos números pares: ")
inicio = int(input("inicio: "))
fim = int(input("fim: "))
print("\033[31mOs números pares ente {} e {} são: \033[m".format(inicio,fim))
for k in range(inicio , fim + 1):
    if k % 2 == 0:
        print(k," " ,end='')