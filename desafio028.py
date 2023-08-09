import random

print("Tente adivinhar o número que pensei de 0 á 10")
n = int(input("Em que número eu pensei? \n"))

r = random.randint(0, 10)

if n == random :
    print("Parabéns, Você acertou o número!")
else: 
    print("Você não conseguiu acertar...")
    
print(" O número escolhido foi: \n {}".format(r))
