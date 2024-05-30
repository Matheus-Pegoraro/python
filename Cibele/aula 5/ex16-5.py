import os
os.system("cls")

print("Algoritmo que mostra a área de um cômodo em metros quadrados e a potência necessária para iluminar esse cômodo ")

largura = float(input("Digite a largura do cômodo em metros: "))

comprimento = float(input("Digite o comprimento do cômodo em metros: "))

m2 = largura * comprimento
pot = m2 *18
print(f"O cômodo tem {m2} metros qudrados.\nSerão necessarios {pot}W para iluminar esse cômodo.")