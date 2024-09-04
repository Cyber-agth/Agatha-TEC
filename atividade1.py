

lista= []

for i in range(1,4):
    while True:
        numero = input(f'Digite o {i}º numero:')
        if numero.isdigit():
            numero= int(numero)
            lista.append(int(numero))
            break
        else:
            print('O numero é um texto, tente novamente!')

for a in lista:
    for b in lista:
        for c in lista:
            print(a, b, c)
        
    

    