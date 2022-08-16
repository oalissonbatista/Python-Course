#Taximetro
distancia = float(input("Qual a distância da viagem?"))
if distancia <= 200:
    valor = 0.50*distancia
    print("O valor da viagem será R${:.2f}".format(valor))
else:
    valor = 0.45*distancia
    print("O valor da viagem será R${:.2f}".format(valor)) 