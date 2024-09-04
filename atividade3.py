linhas= 4
colunas= 4

matriz= []

for i in range(linhas):
    lista = []
    for a in range(colunas):
        if i == a: 
            lista.append(1)
        else:
            lista.append(0)
    matriz.append(lista)
print('matriz 4x4:')

for lista in matriz:
    print(lista)
