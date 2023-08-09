d = int(input("Por quantos dias o carro foi aluagado? \n"))
km = float(input("Quantos km foram percorridos? \n"))

t = (d * 60) + (km * 0.15)

print(f"O preço total a ser pago pelo aluguel de {d} e {km}Km rodados é de, {t}")
