import os
os.system('cls')

print('Desafio')

salario_minimo = float(input('Digite o valor do salário mínimo: '))
os.system('cls')

horas = float(input('Digite o número de horas trabalhadas: '))
os.system('cls')

print('''Tipos de turno\nM = Matutino\nV =Vesperino\nN = Noturno''')
turno = input('Digite o turno em que trabalha: ')
os.system('cls')

print('''Tipos de Cargo\nO = Operário\nG = Gerente: ''')
cargo = input('Digite o cargo que exerce: ')

os.system('cls')

if horas >= 1 and ((turno.upper() == 'M' or turno.upper() == 'V' or turno.upper() == 'N') and (cargo.upper() == 'O' or cargo.upper() == 'G')):
    if turno.upper() == 'M':
        coef = salario_minimo * 0.10
    elif turno.upper() == 'V':
        coef = salario_minimo * 0.15
    else:
        coef = salario_minimo * 0.12

    salario_bruto = horas * coef

    if cargo.upper() == 'O':
        if salario_bruto >= 300:
            imposto = salario_bruto * 0.05
        else:
            imposto = salario_bruto * 0.03
    else:
        if salario_bruto >= 400:
            imposto = salario_bruto * 0.06
        else:
            imposto = salario_bruto * 0.04
        
    if turno.upper() == 'N' and horas > 80:
        gratif = 50
    else: 
        gratif = 30

    if cargo.upper() == 'O' and coef <= 25:
        alimentacao = 50
    else:
        alimentacao = 30

    salario_liq = salario_bruto - imposto + gratif + alimentacao
    
    if salario_liq < 350:
        remu = ('Mal Remunerado')
    elif salario_liq >= 350 and salario_liq <= 600:
        remu = ('Normal')
    else:
        remu =  ('Bem remunerado')

    print(f''' O coeficiente do salário é de: {coef}\nO salário bruto é de: {salario_bruto}\nO imposto é de: {imposto}\nA gratificação é de: {gratif}\nO auxílio alimentção é de: {alimentacao}\nO salário líquido é de: {salario_liq}\nO Indivíduo tem a remuneração considerada: {remu}''')
else:
    print('Informações Inválidas')
    