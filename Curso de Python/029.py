#Pardal
velocidade = float(input("Qual a velocidade do carro?"))
if velocidade >80:
    print("MULTADO! Você excedeu o limite de velocidade que é de 80Km/h")
    valor = ((velocidade - 80)*7)
    print("O valor da multa é de R${:.2f}".format(valor))
else: 
    print("Velocidade normal")