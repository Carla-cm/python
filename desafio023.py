num= int(input("Digite um número de 0 á 9999 : \n"))

n = str(num)

print("Analisando o numero {}".format(num))
print("A unidade: {}".format(n[3]))
print("A dezena: {}".format(n[2]))
print("A centena: {}".format(n[1]))
print("Milhar: {}".format(n[0]))
