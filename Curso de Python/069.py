maiores = Fmenor20 =  homens = 0
while True:
    print("-"* 20 + "\nCadastre uma pessoa\n" + "-"*20)
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in "FM":
        sexo = str(input("Sexo [F/M]: ")).upper().strip()[0]
    if idade >= 18:
        maiores +=1
    if sexo == 'M':
        homens +=1
    if sexo == 'F' and idade < 20:
        Fmenor20 +=1
    continuar = input("Quer continuar?").upper().strip()[0]
    if continuar == "N":
        print(f"""
Voce cadastrou {maiores} pessoa(s) maior(es) de 18 anos, {homens} 
homens e {Fmenor20} mulher(es) menor(es) de 20 anos""")
        break