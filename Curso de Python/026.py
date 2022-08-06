frase = str(input("Digite uma frase: ")).upper().strip()
# contragem de string
count = frase.count('A')
a = frase.find('A') +1
ultimo = frase.rfind('A')+1

print("A frase possui {} letras a, aparece pela primeira" 
"vez na {} posção e na ultima vez na {} posção".format(count,a,ultimo))