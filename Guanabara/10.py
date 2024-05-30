import os
os.system("cls")

print("Algoritmo que recebe  as dimensões de uma parede e calcula o quanto de tinta é necessário para pinta-la")

al = float(input("Digite a altura da parede: "))
la = float(input("Digite a largura da parede: "))
m2 = la * al
tinta = m2 / 2

print(f"Serão necessários {tinta} litros de tinta para pintar a parede por completo.")
