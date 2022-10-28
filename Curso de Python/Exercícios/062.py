inicio = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))
termo = inicio
cont =1
total = 0 
mais = 10
while mais != 0: 
    total += mais   
    while cont <= total:   
        print("{}".format(termo), end = " - ")
        cont += 1
        termo += r 
    print('PAUSA')
    mais = int(input(("Deseja mostrar mais quantos termos? ")))
print("Progressão finalizado após {} termos.".format(cont-1))



