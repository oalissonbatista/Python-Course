cont = mult = 0
n = int(input("Deseja a tabuada de qual número? "))
if n > 0:
    print("-"*7+  "Tabuada"+ "-"*7)
while True:
    if n < 0:
        print("PROGRAMA ENCERRADO.")
        break
    cont += 1
    mult = n* cont
    print(f"{n} x {cont} = {mult}")
    if cont == 10:
        break
