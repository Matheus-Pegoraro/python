import random 
import os
os.system('cls')
print('jogo da sorte')

x = random.randint(1, 5)
y = float(input('Digite um número de 1 a 5: '))
if y == x:
    print(f'''você venceu!\nO número sorteado é: {x}''')
else:
    print(f'''se fodeu\nO número sorteado é: {x}''')