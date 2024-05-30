import os
os.system("cls")

print("Algoritmo que fornece o número de igressos que devem ser vendidos para abater o valor do custo do espetáculo")

custo = float(input("Digite o custo total do espetáculo: "))

preco = float(input("Digite o preço do ingresso: "))

meta = custo/preco

print(f"Será preciso vender {meta:.0f} ingressos para abater o custo.")