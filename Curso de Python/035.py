r1 = float(input("Digite o comprimento da Reta 1:"))
r2 = float(input("Digite o comprimento da Reta 2:"))
r3 = float(input("Digite o comprimento da Reta 3:"))

if ((r1 + r2) > r3) and ((r1 + r3) > r2) and ((r2 + r3 ) > r1): 
    print ("Pode formar triângulo")
else:
    print("Não pode formar triângulo")