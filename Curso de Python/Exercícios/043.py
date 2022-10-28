peso = float(input("Qual o seu peso: "))
altura = float(input("Qual a sua altura: "))
imc = peso / (altura**2)
print("Seu IMC é de {:.1f}".format(imc))
if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc >= 18.5 and imc < 25:
    print("Você está com um peso ideal.")
elif imc >= 25 and imc <= 40:
    print("Você está com obesidade.")
else:
    print("Você está com obesidade mórbida, cuidado.")