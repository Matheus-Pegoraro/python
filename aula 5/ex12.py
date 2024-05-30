import os
os.system("cls")

print("Algoritmo que fornece e média final do aluno")

nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

nota3 = float(input("Digite a terceira nota: "))

mf = (nota1 * 2 + nota2 * 3 + nota3 * 5)/10

os.system("cls")

print(f"A média final do aluno é: {mf}")
