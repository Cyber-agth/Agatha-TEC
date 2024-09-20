matriz = [
    [8,9,4],
    [5,1,3],
    [5,8,9]
    ]


transposta = []


for i in range(len(matriz)):
    linha = []
    for b in range(len(matriz[i])):
        linha.append(matriz[b][i])
    transposta.append(linha)
        




for i in range(3):
    for b in range(3):
        print(f'  {transposta[i][b]}', end='')
    print('')