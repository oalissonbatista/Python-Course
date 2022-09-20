f = str(input("Digite uma frase: "))
fsem= f.replace(" ","")
print(fsem)

if fsem == "".join(reversed(fsem)):
    print("é palindromo") 
else:
    print("não é palíndromo")


