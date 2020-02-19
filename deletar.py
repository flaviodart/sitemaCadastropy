def deletar(cpf,usuarios):
    arq = open('cadastros.txt','r+')
    linhas = arq.readline()
    for linha in linhas:
        if cpf in linha:
            print(cpf)
            linha = linha.replace(linha,'')
            print(linha)
    print(linha)        

    arq.close()
        
