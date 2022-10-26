cont = 0
mult = 0

while cont < 10:
    n = int(input("Deseja a tabuada de qual número? "))
    print("-"*7+  "Tabuada"+ "-"*7)
    if n < 0:
        break
    cont += 1
    mult = n* cont
    print(f"{n} x {cont} = {mult}")
