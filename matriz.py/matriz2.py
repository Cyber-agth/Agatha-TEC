
matriz= [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

soma_total= 0


#percorrendo a matriz
for i in range (len(matriz)):
    print(f'{matriz[i]}\n' , end='')



#soma da matriz 
for i in matriz:
    for elemento in i:
        soma_total += elemento
print(f"\nSoma total: {soma_total}\n")




#soma das linhas da matriz
soma= []
for a in range(len(matriz)):
    soma_linhas=0
    for i in range(len(matriz[a])):
        soma_linhas += matriz[a][i]
    soma.append(soma_linhas)
print(f"Soma das linhas: {soma}\n")



#soma das colunas da matriz
list=[]
for i in range(len(matriz)):
    soma_colunas = 0
    for b in range(len(matriz[i])):
        soma_colunas += matriz[b][i]
    list.append(soma_colunas)
print(f"Soma das colunas: {list}\n") 


#inverção da matriz

transposta = []


for i in range(3):
    linha = []
    for b in range(3):
        linha.append(matriz[b][i])
    transposta.append(linha)
        

for i in range(3):
    for b in range(3):
        print(f'  {transposta[i][b]}', end='')
    print('')



