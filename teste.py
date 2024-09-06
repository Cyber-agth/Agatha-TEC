import PySimpleGUI as sg
import time

layout = [[sg.Text('Bem-vindo ao App com Animação!', font=('Helvetica', 16))]]

# Inicialmente, a janela será completamente transparente (alpha_channel=0)
window = sg.Window('Janela com Fade-In', layout, alpha_channel=0)

# Gradualmente aumentando a transparência
for i in range(0, 101, 5):  # Passos de 5% a cada iteração
    window.TKroot.attributes('-alpha', i/100)  # i/100 converte a porcentagem em alpha de 0 a 1
    window.refresh()  # Atualiza a janela
    time.sleep(0.05)  # Pausa para criar o efeito de animação

event, values = window.read()
window.close()
