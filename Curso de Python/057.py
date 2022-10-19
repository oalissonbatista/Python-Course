#sexo masculino ou feminino;
n = 0
while n != 'M' and n != "F":    #while sexo not in 'MmFf':
    n = input("Qual o seu sexo? F ou M? ").strip().upper()[0]
    if n !='M' and n != 'F':
        print("\033[35mValor não permitido, digite novamente. \033[m")
    if n == 'M':
        print("Você é do sexo Masculino")
    elif n == 'F':
        print("Você é do sexo feminino")
print("fim")