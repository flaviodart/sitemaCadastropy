def pesquisar(cpf,usuarios):
    arq = open('cadastro.txt','r')
    for linha in arq.readlines():
        if cpf in linha:
            return linha
        else:
            return 'Usuário não cadastrado'
            
    arq.close()        
