r1 = float(input("Digite o comprimento da Reta 1:"))
r2 = float(input("Digite o comprimento da Reta 2:"))
r3 = float(input("Digite o comprimento da Reta 3:"))
 
if ((r1 + r2) > r3) and ((r1 + r3) > r2) and ((r2 + r3 ) > r1): 
    print ("Os segmentos podem formar um triângulo ", end = '')
    if r1 == r2 == r3:
        print("Equilátero")
    elif r1 == r2 or r1 == r3 or r3 == r2:
        print("Isóceles.")
    elif r1 != r2 != r3:
        print("Escaleno")
else:
    print("Os segmentos não podem formar um triângulo.")