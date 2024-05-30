
import random
import os
os.system('cls')
print('Jogo da sorte')

x = random.randint(1, 10)
t = 1

while True:
    y = int(input('Digite um número de 1 a 10: '))
    if y == x:
        break
    else:
        print('Você errou, tente novamente.')
        t = t + 1

print(f'Você acertou em {t} tentativas.')