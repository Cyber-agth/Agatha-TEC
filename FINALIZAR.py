import PySimpleGUI as sg

def finalizar(alunos):
    melhor_aluno = None
    melhor_nota = 0

    # RESUMO ALUNOS
    layout = [
        [sg.Text('Lista de alunos')],
        [sg.Listbox(values=[f"Nome: {aluno['nome']}, Média: {aluno['media']}, Aproveitamento: {aluno['aproveitamento']}, Situação: {aluno['situação']}" for aluno in alunos], size=(60, 10), key='-ALUNOS-')],
        [sg.Button('Voltar'), sg.Button('Melhor Aluno')]
    ]

    # Criação da Janela
    window = sg.Window('Alunos', layout)

    # Loop de Eventos para processar "eventos" e obter os "valores" das entradas
    while True:
        event, values = window.read()

        # Se o usuário fechar a janela ou clicar em "Voltar"
        if event == sg.WIN_CLOSED or event == 'Voltar':
            break

        if event == 'Melhor Aluno':
            for aluno in alunos:
                if aluno['media'] > melhor_nota:
                    melhor_nota = aluno['media']
                    melhor_aluno = aluno
            
            if melhor_aluno:
                sg.popup(f"Melhor Aluno: {melhor_aluno['nome']}\nMédia: {melhor_aluno['media']}\nAproveitamento: {melhor_aluno['aproveitamento']}\nSituação: {melhor_aluno['situação']}")

    window.close()

# Exemplo de uso
alunos = [
    
]

finalizar(alunos)
