print("Descubra se o ano é bissexto.")
a = int(input("Qual ano que quer analisa: \n"))

if a % 4 == 0:
    print("O ano {} é bissexto.".format(a))
else:
    print("O ano {} não é bissexto.".format(a))
