import os
os.system("cls")

print("Algoritmo que recebe algo e forneçe seu tipo primitivo, além de algumas informações sobre")

info = input("Digite algo: ")

try:
    vint = int(info)
    print("O que voce digitou é um valor numérico inteiro")
except ValueError:

    try:
        vfloat = float(info)
        print("O que voce digitou é um valor numérico real.")
    except ValueError:
        print("O que voce digitou é um valor Alfabético.")
        print(f"O que voce digitou esta totalmente em maiúsculo? {info.isupper()}")
        print(f"O que voce digitou está totalmente em minúsculo? {info.islower()}")



