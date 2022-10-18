#sexo masculino ou feminino;
n = 0
while n != 'M' and n != "F":    
    n = input("Qual o seu sexo? ").upper()
    if n !='M' and n != 'F':
        print("\033[35mValor não permitido, digite novamente. \033[m")
    if n == 'M':
        print("Você é do sexo Masculino")
    elif n == 'F':
        print("Você é do sexo feminino")
print("fim")