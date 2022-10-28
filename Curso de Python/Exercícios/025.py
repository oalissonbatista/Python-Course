from xmlrpc.client import boolean
# Verificação de nome
nome = str(input("Digite o nome completo: "))
separado = (nome.upper().split())
procurando = separado.count('SILVA')
print("O nome tem Silva? {}".format(boolean(procurando)))