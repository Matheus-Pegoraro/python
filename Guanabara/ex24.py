import os


os.system('cls')

print('Identificador de Sexo')
sx = input('Digite o seu sexo (M/F): ').upper()
while sx != 'M' and sx != 'F':
    sx = input('Sexo errado, digite novamente: ').upper()
    os.system('cls')
if sx == 'M':
    print('Voce e homem')
else:
    print('Voce e mulher')
