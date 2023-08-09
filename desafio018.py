import math

an = float(input("Digite o valor ângulo: \n"))
s = math.sin(math.radians(an))

print("O ângulo de {} tem o SENO de {:.2f}".format(an, s))

c = math.cos(math.radians(an))

print("O ângulo de {} tem o COSSENO de {:.2f}".format(an, c))

t = math.tan(math.radians(an))
print("O ângulo de {} tem o TANGENTE de {:.2f}".format(an, t))
