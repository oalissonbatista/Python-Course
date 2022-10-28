#Aula 15 - Interropendo repetições While com o break.
n=0
while n <= 10:
    n = int(input("Digite um numero: "))
    if n == 5:
        break
    print("Hello") 
print(f"{n:-^20}") 