import os
os.system("cls")

print("Algoritmo que recebe a quantidade de dias alugados para um carro e a quilometragem roadada com ele e calcula o quanto a pagar.")

d = float(input("Digite por quantos dias o carro foi alugado: "))
km = float(input("Digite o quanto o carro rodou nesses dias (Km): "))
pagar = d * 60 + km * 0.15

print(f"O total a pagar será: {pagar}R$ ")
