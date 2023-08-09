f = str(input("Digite uma frase: \n")).upper().strip()

print("A letra A aparece {} vezes na frase. ".format(f.count("A")))

print("A primeira letra A apareceu na posição {}.".format(f.find("A")+1))

print("A última letra A aparece na posição {}.".format(f.rfind("A")+1))
