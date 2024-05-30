import os
os.system("cls")
print("Agenda")
agenda = []
dados = []
op = 0
while op != 6:
    print("1 Cadastrar")
    print("2 - Listar")
    print("3 - Listar determinado amigo")
    print("4 - Alterar por nome")
    print("5 - Excluir por nome")
    print("6 - Sair")
    op = int(input("Digite sua opção: "))
    match op:
        case 1:
            dados.append(input(f"Digite o nome: ").upper())
            dados.append(input(f"Digite o email: "))
            dados.append(input(f"Digite o celular: "))
            agenda.append(dados[:])
            dados.clear()
        case 2: 
            for e in agenda:
                print("Nome : ",e[0])
                print(f"Email: {e[1]}")
                print(f"Celular: {e[2]}")
                input("pressione enter para continuar")
            os.system('cls')
        case 3:
            most = (input('Digite o nome do usuário: ').upper())
            achou = 0
            for i in agenda:
                if most == i[0]:
                    print(i[1])
                    print(i[2])
                    achou = achou + 1
            if achou == 0:
                print('Usuário não cadastrado.')
            input("pressione enter para continuar")
            os.system('cls')
        case 4:
            atu = input('Digite o nome do usuário: ').upper()
            achou = 0
                
            for i in range(len(agenda)):
                    if atu == agenda[i][0].upper():
                        achou = 1
                        
                        novo_email = input("Digite o novo email: ")
                        novo_numero = input("Digite o novo número: ")
                        
                        agenda[i] = (atu, novo_email, novo_numero)
                        print("Usuário atualizado com sucesso!")
                        
            if achou == 0:
                print("Usuário não encontrado.")
                input("pressione enter para continuar")
            os.system('cls')
        case 5:
            atu = input('Digite o nome do usuário: ').upper()
            achou = 0
                
            for i in agenda:
                    if atu == i[0].upper():
                        achou = 1
                        
                        agenda.remove(i)
                        
                        print("Usuário deletado com sucesso!")
            if achou == 0:
                print("Usuário não encontrado.")
                input("pressione enter para continuar")
            os.system('cls')