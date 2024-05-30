import os
os.system("cls")

print("Algoritmo que calcula o vaor da hipotenusa a partir dos valores dos catetos.")

ad = float(input("Digite o coprimento o cateto adjacente: "))
op = float(input("Digite o comprimeno o cateto oposto: "))
hip = (ad**2 + op**2) **0.5

print(f"A hipotenusa mede {hip}")