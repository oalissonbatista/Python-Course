from xmlrpc.client import boolean
# verificação de nome
cidade =str(input("Digite o nome da cidade: "))
cidade.capitalize()
separado = cidade.split()
procurando =(separado[0].upper() == "SANTO")

print("O nome da cidade começa com Santo?\n{}".format(boolean(procurando)))