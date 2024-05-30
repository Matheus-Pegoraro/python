import os
import math

os.system("cls")

print("Algoritmo que fornece o seno, o cosseno e a tangente de um angulo.")

an = float(input("Digite o ângulo: "))

if an > 360 or an <=0:
    print("Ângulo inválido")
else:
    sen = math.sin(math.radians(an))
    cos = math.cos(math.radians(an))
    tan = math.tan(math.radians(an))
print(f"O seno, cosseno e tangente do angulo: {an} são repectivamente:\n{sen:.2f}\n{cos:.2f}\n{tan:.2f}")