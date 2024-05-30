import os
from random import choice

os.system("cls")

print("Algoritmo que sorteia nomes.")

nome1 = input("Digite um nome: ")
nome2 = input("Digite outro: ")
nome3 = input("Digite mais um: ")
nome4 = input("Digite o último: ")

nomes = nome1,nome2,nome3,nome4

escolhido = choice(nomes)

print(f"O(A) escolhido(a) para apagar a lousa é: {escolhido}")