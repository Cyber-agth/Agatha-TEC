import PySimpleGUI as sg

jogo_velha= ['']*9
jogadorx= "X"
botao= 1


#matriz invisivel 
matriz_inv= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

layout= [
    [sg.Push(),sg.Text('Jogo da velha'),sg.Push()],
    [sg.Text(f'É a vez do {jogadorx}', key='troca')],
    [sg.Button('Reiniciar')]

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
    global matriz_inv
    ganhou = ''
    #Verificar vitoria em linha e colunas
    for i in range(3):
        #Vitoria em linha
        if matriz_inv[i][0] == matriz_inv[i][1] == matriz_inv[i][2]:
            ganhou = 'S'
            break
        #Vitoria em coluna
        if matriz_inv[0][i] == matriz_inv[1][i] == matriz_inv[2][i]:
            ganhou = 'S'
            break
        #Vitorias em diagonais
        if matriz_inv[0][0] == matriz_inv[1][1] == matriz_inv[2][2]:
            ganhou = 'S'
            break
        if matriz_inv[0][2] == matriz_inv[1][1] == matriz_inv[2][0]:
            ganhou = 'S'
            break
    return ganhou 
    
        
def verificar_empate():
    #Verifica se os botoes estão preenchidos
    for i in range(3):
        for j in range(3):
            if matriz_inv[i][j] in range(1,10):
                return False
    return True # Todos os espaços preenchidos, empate



while True:
    event, values= window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Reiniciar':
        matriz_inv= [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    
        jogadorx = 'X'
        window['troca'].update(f'É a vez do:{jogadorx}')
        for a in range(1,10):
            window[a].update('')
        continue
            
    
    if int(event) >=1 and int(event) <= 9:
        for i in range(3):
            for b in range(3):
                if matriz_inv[b][i] == int(event):
                    matriz_inv[b][i] = jogadorx
                    window[event].update(jogadorx)
                    
                    ganhou = verificar_vencedor()
                    if ganhou == 'S':
                        sg.popup(f'Jogador {jogadorx} venceu!')
                        for a in range(1,10):
                            window[a].update('')

                            matriz_inv= [
                                [1,2,3],
                                [4,5,6],
                                [7,8,9]
                            ]
                            
                            
                    elif verificar_empate():
                        sg.popup('Emapate!')
                        for a in range(1,10):
                            window[a].update('')

                            matriz_inv= [
                                [1,2,3],
                                [4,5,6],
                                [7,8,9]
                            ]
                            
                    else:       

                        jogadorx = 'O' if jogadorx == 'X' else 'X'
                        window['troca'].update(f'É a vez do: {jogadorx}')
                            
window.close()