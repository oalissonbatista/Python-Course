idadetotal = 0 
velho = 0
menos20 = 0
nomevelho = ''
for k in range (1,4+1):
    print("\n------{} PESSOA------".format(k))
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo F ou M? ").upper()
    print("--------------------")
    idadetotal += idade 

    if k ==1 and sexo == 'M':
        velho = idade
        nomevelho = nome
    if sexo == 'M' and idade > velho:
        velho = idade
        nomevelho = nome 
    if sexo == 'F' and idade < 20:
        menos20 += 1
media = idadetotal / 4    

if menos20 == 0:
    print("Nenhuma mulher tem menos de 20 anos ")
else:
    print("{} mulher(es) tem menos de 20 anos".format(menos20))
print("A média de idade do grupo é de {:.2f} anos".format(media))
print("O homem mais velho se chama {}".format(nomevelho))
#print("{} mulheres tem menos de 20 anos".format(menos20))
