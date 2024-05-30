import os
os.system("cls")

print("Algoritmo que fornece o que restará do salário de João quando ele pagar sus contas atrasadas")

salario = float(input("Digite o salário de João em R$: "))

conta1 = float(input("Digite o valor da primeira conta em R$: "))

conta2 = float(input("Digite o valor da segunda conta em R$: "))

resta = salario - (conta1 *1.02 + conta2 *1.02)

print(f"Restará do salário de joão : {resta}R$")