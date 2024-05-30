import os
os.system('cls')

cid =input('Digite o nome da cidade onde mora: ')
splt = cid.split()
if 'SANTO' in splt[0].upper():
    print('O nome da cidade começa com "santo"')
else:
    print('O nome da cidade não começa com "santo"')