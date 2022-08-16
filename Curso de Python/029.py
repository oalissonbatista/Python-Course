#Pardal
velocidade = float(input("Qual a velocidade do carro?"))
if velocidade >80:
    print("Você foi multado por excesso de velocidade")
    valor = ((velocidade - 80)*7)
    print("O valor da multa é de R${:.2f}".format(valor))
else: 
    print("Velocidade normal")