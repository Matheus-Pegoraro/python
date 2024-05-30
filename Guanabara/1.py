import os
os.system("cls")

print("Algoritmo que recebe a as notas de um aluno, calcula suas respectivas méias de cada bimestre e mostra se ele passou ou não.")
os.system("cls")

def validar(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Número inválido, por favor insira um numero entre 0 e 10.")
        except ValueError:
            print("Entrada invalida")


            
nota11 = validar("Digite a primeira nota do primeiro bimestre: ")
nota21 = validar(input("Digite a segunda nota do primeiro bimestre: "))
nota31 = validar(input("Digite a terceira nota do primeiro bimestre: "))
os.system("cls")
nota12 = validar(input("Digite a primeira nota do segundo bimestre: "))
nota22 = validar(input("Digite a segunda nota do segundo bimestre: "))
nota32 = validar(input("Digite a terceira nota do segundo bimestre: "))
os.system("cls")
nota13 = validar(input("Digite a primeira nota do terceiro bimestre: "))
nota23 = validar(input("Digite a segunda nota do terceiro bimestre: "))
nota33 = validar(input("Digite a terceira nota do terceiro bimestre: "))
os.system("cls")
nota14 = validar(input("Digite a primeira nota do quarto bimestre: "))
nota24 = validar(input("Digite a segunda nota do quarto bimestre: "))
nota34 = float(input("Digite a terceira nota do quarto bimestre: "))
os.system("cls")
media1 = (nota11 + nota21 + nota31) / 3
media2 = (nota12 + nota22 + nota32) / 3
media3 = (nota13 + nota23 + nota33) / 3
media4 = (nota14 + nota24 + nota34) / 3
os.system("cls")
mf = (media1 + media2 + media3 + media4) / 4

os.system("cls")
if mf >= 6.0:
    print("Aluno aprovdo")
else:
    print("Aluno reprovado")
