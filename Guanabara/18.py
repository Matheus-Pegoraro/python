import os
import random

os.system("cls")

print("Algoritmo que sorteia uma lista de nomes.")

nome1 = input("Digite um nome: ")
nome2 = input("Digite outro: ")
nome3 = input("Digite mais um: ")
nome4 = input("Digite o último: ")

nomes = [nome1,nome2,nome3,nome4]

random.shuffle(nomes)

print(f"A ordem das apresentaões ficou como: {nomes}")