linhas = 3
colunas = 3

# Corrigindo a matriz, adicionando as vírgulas entre as listas
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Imprimindo o valor na linha 2, coluna 3 (lembrando que o índice começa em 0)
print(matriz[1][2])

# Substituindo o valor na linha 1, coluna 1 por 10
matriz[0][0] = 10

# Loop para exibir os índices das colunas
for i in range(len(matriz)):
    for a in range(len(matriz[i])):
        print(f'{a} ', end='')
    print('')  # Quebra de linha após cada linha de índices

# Exibindo a matriz após a modificação
for linha in matriz:
    print(linha)
