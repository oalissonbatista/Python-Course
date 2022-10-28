num = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez",
"Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")
n = int(input("Digite um número entre 0 e 20: "))
while n < 0 or n > 20 :
    print("Tente novamente.", end=' ')
    n = int(input("Digite um número entre 0 e 20: "))
print(f"\033[31mVocê digitou o número {num[n]}\033[m.")