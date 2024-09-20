import PySimpleGUI as sg

linha = []
for b in range(3):
    linha.append(sg.Button('', size=(6, 3), key= 'identificação'))
layout.append(linha)

layout.append([
    [sg.Text('')], [sg.Text('', key= 'Resultado')]])

layout.append([sg.Text(f'É a vez do: ({Jogador})', key='Jogador')])