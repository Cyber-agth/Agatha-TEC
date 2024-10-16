import PySimpleGUI as sg

jogo_velha = ['']*9
jogadorx = "X"
botao = 1

# matriz invisível 
matriz_inv = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

layout = [
    [sg.Text('Jogo da Velha')],
    [sg.Button('Reiniciar')]
]

# Código para montar o tabuleiro do jogo
for b in range(3):
    linha = []
    for a in range(3):
        linha.append(sg.Button('', size=(6, 3), key=(botao)))
        botao += 1
    layout.append(linha)

window = sg.Window('Jogo da Velha', layout)

def verificar_vencedor():
    global matriz_inv
    # Verifica vitória em linhas, colunas e diagonais
    for i in range(3):
        # Vitória em linha
        if matriz_inv[i][0] == matriz_inv[i][1] == matriz_inv[i][2]:
            return True
        # Vitória em coluna
        if matriz_inv[0][i] == matriz_inv[1][i] == matriz_inv[2][i]:
            return True
    # Vitória em diagonais
    if matriz_inv[0][0] == matriz_inv[1][1] == matriz_inv[2][2]:
        return True
    if matriz_inv[0][2] == matriz_inv[1][1] == matriz_inv[2][0]:
        return True
    return False

def verificar_empate():
    # Verifica se todos os botões foram preenchidos (empate)
    for i in range(3):
        for j in range(3):
            if matriz_inv[i][j] in range(1, 10):
                return False
    return True

def reiniciar_jogo():
    global matriz_inv, jogadorx
    matriz_inv = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    jogadorx = 'X'
    
    # Limpar todos os botões visualmente
    for a in range(1, 10):
        window[a].update('')
    
    # Reseta o tabuleiro
    window.refresh()

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Reiniciar':
        reiniciar_jogo()
    
    if isinstance(event, int) and 1 <= event <= 9:
        for i in range(3):
            for b in range(3):
                if matriz_inv[b][i] == event:
                    matriz_inv[b][i] = jogadorx
                    window[event].update(jogadorx)
                    
                    # Verificar se houve vitória
                    if verificar_vencedor():
                        sg.popup(f'Jogador {jogadorx} venceu!')
                        reiniciar_jogo()
                    
                    # Verificar se houve empate
                    elif verificar_empate():
                        sg.popup('Empate!')
                        reiniciar_jogo()
                    else:
                        # Alterna o jogador
                        jogadorx = "O" if jogadorx == "X" else "X"

window.close()
