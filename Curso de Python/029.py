#Pardal
velocidade = float(input("Qual a velocidade do carro?"))
if velocidade >80:
    print("\033[4;31mMULTADO! Você excedeu o limite de velocidade que é de 80Km/h\033[m" )
    valor = ((velocidade - 80)*7)
    print("\033[4;34mO valor da multa é de R${:.2f}\033[m".format(valor))
else: 
    print("\033[34mVelocidade normal")