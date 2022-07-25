from math import hypot

cto = float(input("Comprimento do Cateto oposto:"))
cta = float(input("Comprimento do Cateto adjacente:"))
hipotenusa = hypot(cto,cta)

print("a hipotenusa do Triangulo retângulo é {:.2f}".format(hipotenusa))