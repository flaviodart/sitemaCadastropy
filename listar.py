def listar():
    arq = open(f'cadastro.txt', 'r')
    cont = 0
    print()
    for linha in arq.readlines():
        print(f'{linha}')
        cont += 1
    print(f'Temos {cont} usuários!')

    arq.close()
