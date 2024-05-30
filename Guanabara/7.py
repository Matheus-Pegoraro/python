import os
os.system("cls")

print("Algoritmo que recebe uma ditância em metros, e transfere para centímetros e milímetros.")

d = float(input("Digite a distância(metros): "))
cm = d * 100
mm = d * 1000

print(f"A distância em centímetros é: {cm}, e em milímetros é: {mm}")
