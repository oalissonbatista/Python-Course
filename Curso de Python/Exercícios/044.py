valor = float(input("Digite o valor do produto: "))
opcao= int(input("\033[31mESCOLHA A FORMA DE PAGAMENTO\033[m\n"
                 "Digite [1] para pagamento à vista ou cheque\n"
                 "Digite [2] para pagamento à vista no cartão\n"
                 "Digite [3] para pagamento em até 2x no cartão\n"
                 "Digite [4] para pagamento em 3x ou mais no cartão\n"))

if opcao == 1:
    print("Com 10% de desconto ficou R${:.2f}".format(valor-(valor*(10/100))))
elif opcao == 2:
    print("À vista no cartão com 5% de desconto ficou R${:.2f}".format(valor-(valor*(5/100))))
elif opcao == 3:
    print("2x no cartão e sem desconto, ficou R${:.2f}, 2x de R${:.2f}".format(valor,valor/2))
elif opcao == 4:
    total = valor + (valor*(20/100))
    print("em 3x ou mais no cartão, com 20% de juros, ficou R${:.2f}".format(total))
    parcelas = int(input("Em quantas parcelas? "))
    valorParcelas = (total) / parcelas
    print("Ficou {:.2f} em {}x de R${:.2f} ".format(total, parcelas, valorParcelas))
else:
    print("\033[31mOpção inválida de pagamento, tente novamente.\033[m")