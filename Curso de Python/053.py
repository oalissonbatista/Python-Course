f = (str(input("Digite uma frase: "))).strip().upper()
fsem= f.replace(" ","")
inverso = ''
print(fsem)
#print("".join(reversed(fsem)))
for letra in range(len(fsem) -1, -1, -1):
    inverso += fsem[letra]
print (inverso)
if inverso == fsem:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")


#if fsem == "".join(reversed(fsem)):
 #   print("é palindromo") 
#else:
#    print("não é palíndromo")


