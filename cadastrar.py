def cadastrar(lista):
    '''
    Função cadastra dados no arquivo texto
    '''
    arq = open(f'cadastro.txt', 'a')
    for i in lista:
        cont = 0
        for j in i:
            cont += 1
            arq.write(j)
            if cont < len(j):
                arq.write(';')
        arq.write('\n')

    arq.close()
