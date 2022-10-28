inicio = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))
termo = inicio
cont = 1
while cont <= 10 :
    print("{}".format(termo), end = ' ')
    print('>> ' if cont < 10 else "", end = '' )
    termo += r
    cont += 1
    
