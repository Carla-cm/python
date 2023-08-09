km = float(input("Qual é a distância da sua viagem? \n"))
print("Você está prestes a fazer uma viagem de {}Km".format(km))

valor = km * 0.5
valor2 = km * 0.45

if km < 200:
    print("O valor da sua passagem será de R${:.2f}.".format(valor))
else: 
    print("O valor da sua passagem será de R${:.2f}.".format(valor2))
    
