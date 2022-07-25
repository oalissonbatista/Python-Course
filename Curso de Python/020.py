from random import shuffle
Primeiro = str(input('Primeiro nome: '))
Segundo = str(input('Segundo nome: '))
Terceiro = str(input('Terceiro nome: '))
Quarto = str(input('Quarto nome: '))
lista = [Primeiro,Segundo,Terceiro,Quarto]
shuffle(lista) 

print('A ordem de apresentação será:{}'.format(lista))