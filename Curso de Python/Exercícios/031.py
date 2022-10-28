#Taximetro
distancia = float(input("Qual a distância da viagem?"))
# preço= distancia * 0.50 if distancia <=200 else distancia * 0.45
if distancia <= 200:
    valor = 0.50*distancia
    print("O valor da viagem será R${:.2f}".format(valor))
else:
    valor = 0.45*distancia
    print("O valor da viagem será R${:.2f}".format(valor)) 