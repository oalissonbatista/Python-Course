#Aumento salario
from time import sleep
salario = float(input("Digite o salario do funcionario:"))
if salario > 1250:
    aumento = (10/100)*salario
    novoSalario = salario + aumento
    print("CALCULANDO AUMENTO...")
    sleep(2)
    print("Com aumento de R${:.2f} o salário passará a ser de R${:.2f}".format(aumento, novoSalario))
else:
    aumento = (15/100)*salario
    novoSalario = salario + aumento
    print("CALCULANDO AUMENTO...")
    sleep(2)
    print("Com aumento de R${:.2f} o salário passará a ser de R${:.2f}".format(aumento,novoSalario))
print("----Fim----")
    