import PySimpleGUI as sg

jogo_velha= ['']*9
jogadorx= "X"
botao= 1
jogadas=[]

#matriz invisivel 
matriz_inv= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

layout= [
    [sg.Text('Jogo da velha')]

]

#CODIGO DO JOGO
for b in range(3):
    linha = []
    for a in range(3):
        linha.append(sg.Button('', size=(6, 3), key= (botao)))
        botao += 1
    layout.append(linha)


window = sg.Window('Jogo da velha', layout)



def verificar_vencedor():
    #Verificar linhas e colunas
    for i in range(3):
        #linhas
        if matriz_inv[i][0] == 'X' and matriz_inv[i][1] == 'X' and matriz_inv[i][2] == 'X':
            return True
    return False
        

while True:
    event, values= window.read()

    if event == sg.WIN_CLOSED:
        break
    
    if int(event) >=1 and int(event) <= 9:
        for i in range(3):
            for b in range(3):
                if matriz_inv[b][i] == int(event):
                    matriz_inv[b][i] = jogadorx
                    window[event].update(jogadorx)
                    jogadas.append(event)
        print(matriz_inv)


        if event:
            print(f'Botão {event} clicado!')

        if verificar_vencedor():
            sg.popup(f'Jogador {jogadorx} venceu!')
            jogadorx = 'X'
            jogadas=[]
            jogo_velha= [0]*9
            for a in range(1,10):
                window[a].update('')
            continue

        else:
            jogadorx = 'O' if jogadorx =='X' else 'X'

                    

window.close()