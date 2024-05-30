import os
os.system("cls")

print("Algoritmo que recebe uma quantia em R$ e converte em US$.")

rs = float(input("Digite a quantia(R$): "))
us = rs / 3.27

print(f"A quantia em dólares é: {us:.2f}")
