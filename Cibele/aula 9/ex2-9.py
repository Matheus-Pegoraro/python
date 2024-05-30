import os
os.system('cls')

print('Jogo do advinha')
valid = 1
twoValid = 0
cont = 0
while valid ==  1:
    try:
        j1 = int(input("Digite um número: "))
        if j1 <= 10 :
            valid = 0 
            twoValid = 1
        else:
            print("Digite um número de 1 a 10.")
           
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
        

os.system('cls')

while cont < 10:
    while twoValid == 1 :
        try:
            j2 = int(input("Advinhe o número digitado pelo Jogador 1.: "))
            if j2 <= 10 :
                break
            else:
                print("Digite um número de 1 a 10.")
        except ValueError:
            print("Digite um número de 1 a 10.")

if j2 == j1:
         cont = cont + 10
         twoValid = 0 
else: 
        cont = cont + 1
print(f'Você acertou em {cont - 9} tentativas! o número era {j1}')