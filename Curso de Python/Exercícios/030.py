#numero par ou impar
from time import sleep
numero = float(input("Digite um número:"))
print("PROCESSANDO...")
sleep(2)
if (numero%2) == 0:
    print("{} é PAR".format(numero))
else: 
    print("{} é ÍMPAR".format(numero))
