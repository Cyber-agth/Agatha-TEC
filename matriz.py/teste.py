matriz= [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range (len(matriz)):
    soma=0
    for elemento in range(len(matriz[i])):
        print(f'{matriz[i][elemento]}  ' , end='')

    print('')