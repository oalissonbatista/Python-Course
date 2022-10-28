nome = input("Digite seu nome completo: ").strip()
# 
separado = nome.split()
Primeiro= separado[0]
Ultimo = separado[-1]
print("--------Muito prazer em te conhecer --------")
print("Nome completo: {}\nPrimeiro nome: {}\nUltimo nome: {}".format(nome,Primeiro,Ultimo))