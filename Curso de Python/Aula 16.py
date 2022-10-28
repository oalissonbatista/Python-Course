#Tuplas - variável composta
#Tuplas são imutáveis

lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

for c in lanche:
    print(c)
print(len(lanche))

for cont in range(0, len(lanche)):
    print (cont,lanche[cont])

for pos,comida in enumerate(lanche):
    print(pos, comida)

#sorted = colocar em ordem
# count() = contar 
# index() = posição de um elemento