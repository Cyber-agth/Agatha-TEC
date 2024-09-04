import PySimpleGUI as sg

def finalizar(alunos):
    melhor_aluno = 0
    melhor_nota = 0

    # RESUMO ALUNOS
    layout = [
        [sg.Text('Lista de alunos')],
        [sg.Listbox(values=[f"Nome: {aluno['nome']}, Média: {aluno['media']}, Aproveitamento: {aluno['aproveitamento']}, Situação: {aluno['situação']}" for aluno in alunos], size=(60, 10), key='-ALUNOS-')],
        [sg.Button('Voltar'), sg.Button('Melhor Aluno')]
    ]
                
    # Create the Window
    window = sg.Window('Alunos', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        # if user closes window or clicks cancel
        if event == sg.WIN_CLOSED or event == 'Voltar':
            break

        if event == 'Melhor Aluno':
            for aluno in alunos:
                if aluno['media'] > melhor_nota:
                    melhor_nota = aluno['media']
                    melhor_aluno = aluno
                    
            if melhor_aluno:
                sg.popup(f"Melhor aluno: {melhor_aluno['nome']}, média: {melhor_aluno['media']}, aproveitamento {melhor_aluno['aproveitamento']}, situação: {melhor_aluno['situação']}")
                
    window.close()

def nota():
    alunos = []
    
    # All the stuff inside your window.
    layout = [
        [sg.Text("Nome do aluno:")],
        [sg.InputText(key='nome')],
        [sg.Text("Primeira nota:")],
        [sg.InputText(key='nota1')],
        [sg.Text('Segunda nota:')],
        [sg.InputText(key='nota2')],
        [sg.Text('Média: ', size=(30, 1)), sg.Text('', key='media')],
        [sg.Text('Aproveitamento: ', size=(30, 1)), sg.Text('', key='aproveitamento')],
        [sg.Text('Situação: ', size=(30, 1)), sg.Text('', key='situação')],
        [sg.Button('Calcular'), sg.Button('Cancelar'), sg.Button('Finalizar')]
    ]
                
    # Create the Window
    window = sg.Window('Cadastro de Alunos', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        # if user closes window or clicks cancel
        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break

        if event == 'finalizar':
            if alunos == []:
                sg.popup('LISTA VAZIA')
            else:
                window.close()
                finalizar(alunos)

        # VALIDANDO OS INPUTS
        if event == 'Calcular':
            nome = values['nome']
            nota1 = values['nota1']
            nota2 = values['nota2']

            if nome == "" or nota1 == "" or nota2 == "":
                sg.popup('ERRO! Insira todos os dados para continuar!')
                continue

            if nome.isdigit():
                sg.popup('ERRO! O nome deve ser texto.')
                continue

            elif len(nome) < 3:
                sg.popup('ERRO! O nome deve ter pelo menos 3 caracteres.')
                continue

            else:
                if nota1.replace('.', '', 1).isdigit() and nota2.replace('.', '', 1).isdigit():
                    nota1 = float(nota1)
                    nota2 = float(nota2)

                    if nota1 > 10 or nota2 > 10:
                        sg.popup('ERRO! O sistema não aceita notas maiores que 10.')
                        continue
                    else:
                        media = (nota1 + nota2) / 2

                        if media >= 9:
                            aproveitamento = 'A'
                        elif media >= 8:
                            aproveitamento = 'B'
                        elif media >= 7:
                            aproveitamento = 'C'
                        elif media >= 6:
                            aproveitamento = 'D'
                        elif media >= 5:
                            aproveitamento = 'E'
                        else:
                            aproveitamento = 'F'

                        situação = 'Aprovado' if media >= 6 else 'Reprovado'

                        window['media'].update(f'{media:.2f}')
                        window['aproveitamento'].update(aproveitamento)
                        window['situação'].update(situação)

                        alunos.append({'nome': nome, 'media': media, 'aproveitamento': aproveitamento, 'situação': situação})
                        window['nome'].update('')
                        window['nota1'].update('')
                        window['nota2'].update('')

                else:
                    sg.popup('ERRO! As notas devem ser números.')
            
                sg.popup(f'A média do aluno {nome} é: {media:.2f}. Aproveitamento: {aproveitamento}. Situação: {situação}')

    window.close()

def cadastro():
    # Todas as coisas dentro da janela.
    layout = [
        [sg.Button('Registrar'), sg.Button('Login')],
        [sg.Text("Nome de usuário")],
        [sg.InputText()],
        [sg.Text("Email")],
        [sg.InputText()],
        [sg.Text("Senha")],
        [sg.Input(password_char='*')],
        [sg.Text("Confirmar senha")],
        [sg.Input(password_char='*')],
        [sg.Button('Entrar')]
    ]

    # Criando a janela
    window = sg.Window('Registrar', layout)

    # Repetição para processar eventos e pegar os valores inseridos nos inputs.
    while True:
        event, values = window.read()

        # Condicional caso o usuário clique no botão 'cancelar' ou clicar no 'X'.
        if event == sg.WIN_CLOSED or event == 'Login':
            break
        if event == 'Entrar':
            window.close()
            nota()

        print('Hello', values[0], '!')

    window.close()

# Todas as coisas dentro da janela.
layout = [
    [sg.Button('Registrar'), sg.Button('Login')],
    [sg.Text("Usuário")],
    [sg.InputText(key='-USUARIO-')],
    [sg.Text('Senha')],
    [sg.Input(password_char='*', key='-SENHA-')],
    [sg.Button('Entrar'), sg.Text('Esqueceu a senha?')]
]

# CRIANDO UMA JANELA
window = sg.Window('Login', layout)

# Event Loop para processar eventos e pegar os valores dos inputs
while True:
    event, values = window.read()

    # Se o usuário fechar a janela ou clicar em cancelar
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'Registrar':
        window.close()
        cadastro()
    
    if event == 'Entrar':
        # Valida se os campos de usuário e senha estão preenchidos
        if not values['-USUARIO-'] or not values['-SENHA-']:
            sg.popup('ERRO! Por favor, preencha todos os campos obrigatórios.')
        else:
            window.close()
            nota()
 
    print('Hello', values[0], '!')

window.close()


