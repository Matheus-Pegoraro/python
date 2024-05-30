import os
os.system("cls")

print("Algoritmo que recebe o salário de um trabahador e fornece seu novo saléario com 15% de aumento.")

s = float(input("Digite o salário em R$: "))
ns = s * 1.15

print(f" O salário com aumento é{ns:.2f}.")
