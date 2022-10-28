#Empréstimo
casa = float(input("\033[31mQual o valor da casa?"))
salario = float(input("\033[34mQual o seu salário?"))
pagamento = float(input("\033[31mA ser pago em quantos anos?"))
prestacao = (casa / (pagamento * 12)) 
aprovacao = (salario* (30/100))

if prestacao > aprovacao:
    print("\033[4;34mInfelizmente o empréstimo foi negado.\033[m")
else:
    print("\033[4;31mParabéns! o empréstimo foi APROVADO!!!\033[m")