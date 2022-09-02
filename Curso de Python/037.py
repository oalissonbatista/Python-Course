num = int(input("\033[34mDigite um número:\033[m"))
escolha = int(input("\033[31mDigite [1] para  Binario\033[m\n\033[32mDigite [2] para Octal"
"\033[m\n\033[33mDigite [3] para Hexadecimal\033[m\nSua opção: " ))
binario = bin(num)
octal = oct(num)
hexa = hex(num)
if escolha == 1:
    print("\033[31m{} em Binário é {}\033[m".format(num,bin(num))) 
elif escolha == 2:
    print("\033[32m{} em Octal é {}\033[m".format(num,oct(num)))
elif escolha == 3:
    print("\033[33m{} em Hexadecimal é {}\033[m".format(num,hex(num)))
else:
    print("Opção inválida, tente novamente.")