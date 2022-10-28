quant = int(input("Quantos termos vc deseja? "))
cont = 3
primeiro = 0
segundo = 1
print ("\033[31m{} - {}".format(primeiro, segundo), end = ' - ')

while cont <= quant:
    terceiro = primeiro + segundo
    cont +=1
    primeiro = segundo
    segundo = terceiro
    print("\033[31m{}\033[m".format(terceiro), end =' - ')
print("Fim")
