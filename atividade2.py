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

for a in range(3):
    for b in range(3):
        for c in range(3):
            if lista[a]!= lista[b] and lista[b]!= lista[c] and lista[a]!= lista[c]: 
                print(lista[a], lista[b], lista[c])
        
    


