import os
os.system('cls')

nome = input('Digite seu nome completo: ')
nomev = nome.strip()
splitnome = nome.split()
lenome = ''.join(splitnome)

os.system ('cls')

print(f'''O nome da pessoa em maiúsculo é: {nomev.upper()}\nO nome da pessoa em minúsculo é: {nomev.lower()}\nO total de caracteres, sem contar espaços é: {len(lenome)}\nO primerio nome tem {len(splitnome[0])} letras.''')
