
matriz= [

    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[1][2])
matriz[0][0]= 10
print(matriz[0][0])

for i in range (len(matriz)):
    soma=0
    for elemento in range(len(matriz[i])):
        print(f'{matriz[i][elemento]} ' , end='')

    print('')

