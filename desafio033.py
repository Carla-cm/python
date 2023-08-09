a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valoe: "))

if a<b and a<c:
    menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
    
print("O menor valor digitado foi: {}".format(menor)) 

if a>b and a >c:
    maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
    
print("O maior valor digitado foi: {}".format(maior))
    