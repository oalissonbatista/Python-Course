km = float(input("Quantos kms percorridos?"))
dias= int(input("Alugado por quantos dias?"))

preço = (60.00*dias) + (0.15*km)

print("O valor do aluguel por {} dias e um rodagem de {}km ficou no valor de R${:.2f}.".format(dias,km,preço))
