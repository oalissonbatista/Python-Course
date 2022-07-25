salario= float(input("Qual o valor do seu salario?")) 
aumento = 15/100 * salario
novoSalario= salario + aumento

print("Com um aumento de R${:.2f}, seu novo salario é de R${:.2f}".format(aumento, novoSalario))