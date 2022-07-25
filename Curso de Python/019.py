from random import choice
Primeiro = str(input('Primeiro aluno: '))
Segundo = str(input('Segundo aluno: '))
Terceiro = str(input('Terceiro aluno: '))
Quarto = str (input('Quarto aluno: '))
lista= [Primeiro,Segundo,Terceiro,Quarto]
sorteado = choice(lista) 

print('O vencedor do sorteio foi: {}. PARABÉNS! {}'.format(sorteado, sorteado))