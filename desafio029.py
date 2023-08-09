v = float(input("Qual velocidade você estava dirigindo? \n"))
m = (v - 80) * 7 

if v > 80:
    print("Você foi MULTADO! Exedeu o limite permitido de 80Km/h. \n O valor da multa é de R${:.2f}".format(m))
else:
    print("Você não exedeu o limite de velocidade da via! ")
