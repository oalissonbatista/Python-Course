from math import cos, sin, tan, radians
# info de ângulos
angulo = float(input("Digite o ângulo:"))
cosseno = cos(radians(angulo))
seno = sin(radians(angulo))
tangente = tan(radians(angulo))

print("O cosseno de {:.2f} é {:.2f}, o seno é {:.2f} e a tangente é {:.2f}".format(angulo, cosseno, seno, tangente))