# Nota de um aluno
individual= float(input("Nota do experimento individual:"))
grupo = float(input("Nota da apresentação em grupo:"))
atividades = float(input("Nota das atividades:"))
nota = ((40/100) * individual) + ((30/100)*grupo) + ((30/100)*atividades)
print("Média Final: {}".format(nota))
