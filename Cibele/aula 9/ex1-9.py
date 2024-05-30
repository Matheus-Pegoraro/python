import os
os.system('cls')

print('Programa que calcula quando a Cidade A vai passar a cidade B')

cont = 0

a = 98000000
b = 200000000

while a < b:
    a = a + a * 0.035
    b = b + b * 0.015
    cont = cont + 1

print(f'''A cidade "A" demorou {cont} vezes para ultrapassar a cidade "B" em número de habitantes''')