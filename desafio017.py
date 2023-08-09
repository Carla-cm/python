from math import hypot


co = float(input("Compriment do cateto oposto: \n"))
ca = float(input("Comprimento do cateto adjacente: \n "))
rq = hypot (co, ca)

print("A hiportenusa vai medir, {:.2f}".format(rq))
