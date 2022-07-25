nomeCompleto = str(input('Digite o nome completo: '))
upperNome = nomeCompleto.upper()
lowerNome = nomeCompleto.lower()
letras = len(nomeCompleto.replace(' ','')) # ou len(nomeCompleto) - nomeCompleto.count(' ')
dividido = nomeCompleto.split()
primeiroNome = len(dividido[0])
print('O nome em upperCase: {}\nEm lowerCase: {} \n'
 'O nome completo possui {} letras \nO primeiro nome tem {} letras'.format(upperNome,lowerNome,letras,primeiroNome))