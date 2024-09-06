import PySimpleGUI as sg
import os


# Função para calcular notas e situações
def nota():
    alunos = []

    layout = [
        [sg.Text("Nome do aluno:")],
        [sg.InputText(key='nome')],
        [sg.Text("Primeira nota:")],
        [sg.InputText(key='nota1')],
        [sg.Text('Segunda nota:')],
        [sg.InputText(key='nota2')],
        [sg.Text('Média:', size=(30, 1)), sg.Text('', key='media')],
        [sg.Text('Aproveitamento:', size=(30, 1)), sg.Text('', key='aproveitamento')],
        [sg.Text('Situação:', size=(30, 1)), sg.Text('', key='situacao')],
        [sg.Button('Calcular'), sg.Button('Cancelar'), sg.Button('Finalizar')]
    ]

    window = sg.Window('Calculadora de Notas', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break

        if event == 'Finalizar':
            if not alunos:
                sg.popup('Lista vazia')
            else:
                window.close()
                finalizar(alunos)

        if event == 'Calcular':
            nome = values['nome']
            nota1 = values['nota1']
            nota2 = values['nota2']

            if not nome or not nota1 or not nota2:
                sg.popup('Erro! Insira todos os dados para continuar!')
                continue

            if nome.isdigit():
                sg.popup('Erro! O nome deve ser texto.')
                continue

            if len(nome) < 3:
                sg.popup('Erro! O nome deve ter pelo menos 3 caracteres.')
                continue

            try:
                nota1 = float(nota1)
                nota2 = float(nota2)
            except ValueError:
                sg.popup('Erro! As notas devem ser números.')
                continue

            if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
                sg.popup('Erro! As notas devem estar entre 0 e 10.')
                continue

            media = (nota1 + nota2) / 2

            if 9 <= media <= 10:
                aproveitamento = 'A'
            elif 8 <= media < 9:
                aproveitamento = 'B'
            elif 7 <= media < 8:
                aproveitamento = 'C'
            elif 6 <= media < 7:
                aproveitamento = 'D'
            elif 5 <= media < 6:
                aproveitamento = 'E'
            else:
                aproveitamento = 'F'

            situacao = 'Aprovado' if media >= 6 else 'Reprovado'

            window['media'].update(f'{media:.2f}')
            window['aproveitamento'].update(aproveitamento)
            window['situacao'].update(situacao)

            alunos.append({'nome': nome, 'media': media, 'aproveitamento': aproveitamento, 'situacao': situacao})

            window['nome'].update('')
            window['nota1'].update('')
            window['nota2'].update('')

            sg.popup(f'A média do aluno {nome} é: {media:.2f}. Aproveitamento: {aproveitamento}. Situação: {situacao}')

    window.close()


# Função para exibir a lista de alunos
def finalizar(alunos):
    melhor_aluno = max(alunos, key=lambda aluno: aluno['media'], default=None)

    layout = [
        [sg.Text('Lista de alunos')],
        [sg.Listbox(values=[f"Nome: {aluno['nome']}, Média: {aluno['media']:.2f}, Aproveitamento: {aluno['aproveitamento']}, Situação: {aluno['situacao']}" for aluno in alunos], size=(60, 10), key='-ALUNOS-')],
        [sg.Button('Sair'), sg.Button('Melhor Aluno')]
    ]

    window = sg.Window('Alunos', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Sair':
            window.close()
            nota()
            break

        if event == 'Melhor Aluno':
            if melhor_aluno:
                sg.popup(f"Melhor aluno: {melhor_aluno['nome']}, Média: {melhor_aluno['media']:.2f}, Aproveitamento: {melhor_aluno['aproveitamento']}, Situação: {melhor_aluno['situacao']}")
            else:
                sg.popup('Nenhum aluno encontrado.')

    window.close()


# Função de cadastro
def cadastro():
    layout = [
        [sg.Button('Registrar'), sg.Button('Voltar')],
        [sg.Text("Nome do usuário")],
        [sg.InputText(key='NOMEUSUARIO')],
        [sg.Text("Email")],
        [sg.InputText(key='EMAIL')],
        [sg.Text("Senha")],
        [sg.InputText(password_char='*', key='SENHA')],
        [sg.Text("Confirmar senha")],
        [sg.InputText(password_char='*', key='CONFIRMAR_SENHA')],
        [sg.Button('Cadastrar')]
    ]

    window = sg.Window('Cadastro', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            window.close()
            break

        if event == 'Voltar':
            window.close()
            login()

        if event == 'Registrar':
            nome = values['NOMEUSUARIO']
            senha = values['SENHA']

            if not nome or not values['EMAIL'] or not senha or not values['CONFIRMAR_SENHA']:
                sg.popup('Erro! Todos os campos são obrigatórios.')
                continue

            if nome.isdigit() or '@' not in values['EMAIL'] or '.' not in values['EMAIL']:
                sg.popup('Erro! O nome e o email devem ser válidos.')
                continue

            if len(nome) < 3 or len(values['EMAIL']) < 3:
                sg.popup('Erro! O nome e o email devem ter pelo menos 3 caracteres.')
                continue

            if senha != values['CONFIRMAR_SENHA']:
                sg.popup('Erro! As senhas não coincidem.')
                continue

            if len(senha) < 5:
                sg.popup('Erro! A senha deve ter pelo menos 5 caracteres.')
                continue

            with open('dados_cadastro.txt', 'a') as file:
                file.write(f"{nome},{senha}\n")

            sg.popup('Cadastro realizado com sucesso!')
            window.close()
            login()

    window.close()


# Função de login
def login():
    layout = [
        [sg.Button('Registrar')],
        [sg.Text("Usuário")],
        [sg.InputText(key='USUARIO')],
        [sg.Text('Senha')],
        [sg.InputText(password_char='*', key='SENHA')],
        [sg.Button('Entrar'), sg.Text('Esqueceu a senha?')]
    ]

    window = sg.Window('Login', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            window.close()
            break

        if event == 'Registrar':
            window.close()
            cadastro()

        if event == 'Entrar':
            if os.path.exists('dados_cadastro.txt'):
                with open('dados_cadastro.txt', 'r') as file:
                    for linha in file:
                        nome, senha = linha.strip().split(',')
                        if nome == values['USUARIO'] and senha == values['SENHA']:
                            sg.popup('Login realizado com sucesso')
                            window.close()
                            nota()
                            break
        
            else:
                sg.popup('Arquivo de cadastro não encontrado.')

    window.close()


login()
