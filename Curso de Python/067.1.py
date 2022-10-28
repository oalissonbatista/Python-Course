while True:
    n = int(input("Deseja ver a tabuada de qual valor? "))
    if n < 0:
        print("Programa encerrado.")
        break
    print("-"*7+"Tabuada"+"-"*7)
    for c in range (1, 10+1):
        print(f"{n} X {c} = {n*c}")