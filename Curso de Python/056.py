idadetotal = 0 
for k in range (1,4+1):
    nome = input("Qual seu nome?")
    idade = int(input("Qual a sua idade?"))
    sexo = input("Qual o seu sexo?")
    idadetotal += idade 

media = idadetotal / 4
print("A média de idade é de {:.0f} anos".format(media))


