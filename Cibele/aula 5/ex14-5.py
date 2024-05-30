import os
os.system("cls")

print("Algoritmo que fornece o peso do indivíduo caso ele engorde 15% e emagreça 20%")

peso = float(input("Digite seu peso atual em Kg:  "))

peso_mais = peso + peso *0.15

peso_menos = peso - peso *0.20

print(f"Se o indivíduo engordar 15% de seu peso ele estará pesando {peso_mais}Kg \nSe o indivíduo emagreçer 20% de seu peso ele estará pesando {peso_menos}Kg ")

