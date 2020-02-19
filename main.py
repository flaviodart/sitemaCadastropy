from listar import *
from mensagem import *
from cadastrar import *
from pesquisar import *
from deletar import *

usuarios = []

opcao = ''
while True:
    print('''
[1] Cadastrar usuário
[2] Pesquisar usuário
[3] Alterar usuário
[4] Excluir usuário
[5] Listar usuários
[0] Sair''')
    
    opcao = input('Digite a opcao desejada: ')
    if opcao == '0':
        break
    while True:
        
        if opcao == '1':
            
            mensagem('CADASTRAR USUÁRIO')
            
            cpf = input('CPF: (Digite 0 se deseja sair) ')
            if cpf == '0':
                break
            cpf = cpf.replace('.','')
            cpf = cpf.replace('-','')
            if len(cpf) != 11:
                print('CPF inválido')
                break

            else:
            
                nome = input('Nome: ')
                
                nome_div = nome.split()
                cpf_div = cpf.split()
                
                op1 = f'{cpf}@ifnet.com.br'
                op2 = f'{nome_div[0]}.{nome_div[-1]}@ifnet.com.br'
                op3 = f'{nome_div[0]}{cpf[0]}{cpf[1]}{cpf[2]}@ifnet.com.br'
                
                print((f'Opções de email: \n1 - {op1}\n2 - {op2}\n3 - {op3}'))
                resp = ''
                while resp not in ['1','2','3']:
                    resp = input('Escolha o email de sua preferência: ')
                
                if resp == '1':
                    usuarios.append([cpf,nome,op1])
                elif resp == '2':
                    usuarios.append([cpf,nome,op2])
                elif resp == '3':
                    usuarios.append([cpf,nome,op3])
                     
                cadastrar(usuarios)
                usuarios = []
                mensagem('CADASTRADO COM SUCESSO')
                         
        elif opcao == '2':
            
            mensagem('PESQUISAR USUÁRIO')
            
            cpf = input('Informe o CPF que deseja buscar: (0 se deseja sair)')
            
            if cpf == '0':
                break
            else:
                pesquisa = pesquisar(cpf,usuarios)
                print(pesquisa)


        elif opcao == '3':
            
            mensagem('ALTERAR USUÁRIO')
            
            cpf = input('Informe o CPF do usuário que deseja alterar: (0 se deseja sair)')
            
            if cpf == '0':
                break
            
            else:
                if cpf in usuarios:
                    #print(f'Cpf: {cpf}\nNome: {usuarios[cpf][0]}\nEmail: {usuarios[cpf][1]}')
                    resp = input('Deseja alterar nome? [S/N]').lower()
                    if resp == 'n':
                        break
                    elif resp == 's':
                        nome = input('Digite novo nome:')
                        #usuarios[1] = nome        
                else:
                    print('Usuário não cadastrado')


        elif opcao == '4':
            
            mensagem('EXCLUIR USUÁRIO')
            
            cpf = input('Informe o CPF que deseja excluir: (0 se deseja sair)')
            
            if cpf == '0':
                break
            
            elif cpf not in usuarios:
                print('Usuário não cadastrado')
                
            else:
                #print(f'Cpf: {cpf}\nNome: {usuarios[cpf][0]}\nEmail: {usuarios[cpf][1]}')
                resp = input('Deseja excluir? [S/N]').lower()
                if resp == 's':
                    deletar(cpf,usuarios)       
                    mensagem('USUÁRIO DELETADO')
                else:
                    break
                

        elif opcao == '5':
            mensagem('LISTAR USUÁRIOS')
            resp = input('Deseja listar usuários? [S/N]').lower()
            if resp == 'n':
                break
            elif resp == 's':
                try:
                    listagemArquivos = listar()
                except:
                    print('Nenhum usuário cadastrado')

        else:
            print('Opção Inválida')
            break
