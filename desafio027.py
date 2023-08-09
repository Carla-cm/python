n = str(input("Digite seu nome completo: \n")).strip()

nome = n.split()

print("Seja bem vindo(a), prazer em te conhecer!")

print("Seu primeiro nome é {}.".format(nome[0]) )
print("Seu último nome é {}".format(nome[len(nome)-1]))
