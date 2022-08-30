r1 = float(input("Digite o comprimento da Reta 1:"))
r2 = float(input("Digite o comprimento da Reta 2:"))
r3 = float(input("Digite o comprimento da Reta 3:"))

if ((r1 + r2) > r3) and ((r1 + r3) > r2) and ((r2 + r3 ) > r1): 
    print ("Os segmentos podem formar um triângulo")
    if r1 == r2 == r3:
        print("Formará um triângulo Equilátero")
    elif r1 == r2 or r1 == r3 or r3 == r2:
        print("Formará um triângulo Isóceles.")
    elif r1 != r2 != r3:
        print("Formará um triângulo Escaleno")
else:
    print("Os segmentos não podem formar um triângulo")