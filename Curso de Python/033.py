n1 = float(input("Digite um número:"))
n2 = float(input("Digite um número:"))
n3 = float(input("Digite um número:"))

if n1 >= n2 >= n3:
    print("{} é o maior".format(n1))
    print("{} é o menor".format(n3))
elif n1 >= n3 >= n2:
    print("{} é o maior".format(n1))
    print("{} é o menor".format(n2))
elif n2 >= n1 >= n3: 
    print("{} é o maior".format(n2))
    print("{} é o menor".format(n3))
elif n2 >= n3 >= n1:
    print("{} é o maior".format(n2))
    print("{} é o menor".format(n1))
elif n3 >= n1 >= n2:
    print("{} é o maior".format(n3))
    print("{} é o menor".format(n2))
elif n3 >= n2 >= n1:
    print("{} é o maior".format(n3))
    print("{} é o menor".format(n1))

else: 
    print("erro")