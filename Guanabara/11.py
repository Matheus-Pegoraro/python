import os
os.system("cls")

print("Algoritmo que recebe o preço do produto e forneceseu novo preço com 5% de desconto.")

p = float(input("Digite o preço do produto em R$: "))
np = p * 0.95

print(f" O valor com desconto é{np:.2f}.")
