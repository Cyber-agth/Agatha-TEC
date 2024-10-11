import PySimpleGUI as sg

jogo_velha = [''] * 9
jogadorx = "X"
botao = 1

# matriz invisível
matriz_inv = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

layout = [
    [sg.Text('Jogo da velha')]
]

# Criar os botões do jogo
for b in range(3):
    linha = []
    for a in range(3):
        linha.append(sg.Button('', size=(6, 3), key=(botao)))
        botao += 1
    layout.append(linha)

window = sg.Window('Jogo da velha', layout)

def reset():
    global jogo_velha, jogadorx, matriz_inv
    jogo_velha = [''] * 9
    jogadorx = 'X'
    matriz_inv = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    for i in range(1, 10):
        window[i].update('')

def verificar_vencedor():
    # Verificar linhas e colunas
    for i in range(3):
        # Vitória em linhas
        if matriz_inv[i][0] == matriz_inv[i][1] == matriz_inv[i][2]:
            return True
        # Vitória em colunas
        if matriz_inv[0][i] == matriz_inv[1][i] == matriz_inv[2][i]:
            return True
    # Vitória nas diagonais
    if matriz_inv[0][0] == matriz_inv[1][1] == matriz_inv[2][2]:
        return True
    if matriz_inv[0][2] == matriz_inv[1][1] == matriz_inv[2][0]:
        return True
    return False

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if int(event) >= 1 and int(event) <= 9:
        for i in range(3):
            for b in range(3):
                if matriz_inv[b][i] == int(event):
                    matriz_inv[b][i] = jogadorx
                    window[event].update(jogadorx)

        if verificar_vencedor():
            sg.popup(f'Jogador {jogadorx} venceu!')
            reset()
        else:
            jogadorx = 'O' if jogadorx == 'X' else 'X'

window.close()


  