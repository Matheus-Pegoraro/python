import os
os.system('cls')

num = int(input('Digite um número de 0 a 9999:'))
if num >= 0 and num <= 9999:
    num_str = str(num)
    split= num_str.zfill(4)
    
    print(f'''A casa do milhar é: {split[0]}\nA casa da centena é: {split[1]}\nA casa da dezena é: {split[2]}\nA casa da unidade é: {split[3]}''')
else:
    print('Numero Inválido')
