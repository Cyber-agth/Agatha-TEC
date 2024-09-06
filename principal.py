import PySimpleGUI as sg
import os



# -------------------------------------------------------- TELA NOTA ------------------------------------------------------

def nota():

    alunos= []
    
   
    layout = [  [sg.Text("Nome do aluno:")],
                [sg.InputText(key= 'nome')],
                [sg.Text("Primeria nota:")],
                [sg.InputText(key= 'nota1')],
                [sg.Text('segunda nota:')],
                [sg.InputText(key= 'nota2')],
                [sg.Text('media: ', size= (30, 1)), sg.Text('',key= 'media')],
                [sg.Text('aproveitamento: ', size= (30, 1)), sg.Text('', key= 'aproveitamento')],
                [sg.Text('situação: ', size=(30,1)), sg.Text('',key='situação')],
                [sg.Button('calcular'), sg.Button('Cancelar'), sg.Button('finalizar')] 
                
                ]

                
    
    window = sg.Window('Hello Example', layout)

    
    while True:
        event, values = window.read()

        
        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break

        if event == 'finalizar':

            if alunos == []:
                sg.popup('LISTA VAZIA')

            else:
                window.close()
                finalizar(alunos)



    #VALIDANDO OS INPUTS
        if event == 'calcular':
            nome = values['nome']
            nota1= values['nota1']
            nota2= values['nota2']



            if values['nome'] == "" or values['nota1'] == "" or values['nota2'] == "": 
                sg.popup('ERRO!, insira os dados para continuar!')
                continue


            if nome.isdigit():
                sg.popup('ERRO!, o nome deve ser texto.')
                continue
               
            
            elif len(nome) <3:
                sg.popup('ERRO!, o nome tem menos de 3 caracteres.')
                continue
                
            else:
                if nota1.isdigit() and nota2.isdigit():
                    nota1= float(nota1)
                    nota2= float(nota2)

                    if nota1 > 10 or nota2 >10:
                        sg.popup('ERRO!, o sistema não aceita notas maiores que 10.')

                    else:
                        media= (nota1 + nota2) / 2


                        if media <= 10 and media >= 9:
                            aproveitamento = 'A'
                        elif media <= 8.9 and media >= 8.0:
                            aproveitamento = 'B'
                        elif media <= 7.9 and media >= 7.0:
                            aproveitamento = 'C'
                        elif media <= 6.9 and media >= 6.0:
                            aproveitamento = 'D'
                        elif media <= 5.9 and media >= 5.0:
                            aproveitamento = 'E'
                        else:
                            aproveitamento = 'F'

                        if media >= 6:
                            situação= 'Aprovado'

                        else:
                            situação= 'Reprovado'


                        window['media'].update(f'{media}')
                        window['aproveitamento'].update(f'{aproveitamento}')
                        window['situação'].update(f'{situação}')
                        

                        alunos.append({'nome': nome, 'media': media, 'aproveitamento': aproveitamento, 'situação': situação})

                        print(alunos)
                        window['nome'].update(f'')
                        window['nota1'].update(f'')
                        window['nota2'].update(f'')

                    
                else:
                    sg.popup('ERRO!, as notas devem ser numeros.')

            
                sg.popup(f'A media do aluno {nome} é: {media}. e o aproveitamento é: {aproveitamento}. situação {situação}')
                        

    window.close()


# ------------------------------------------- POPUP DA LISTA DE ALUNOS ------------------------------------------------

def finalizar(alunos):
    melhor_aluno= 0
    melhor_nota= 0

    layout = [  [sg.Text('Lista de alunos')],
                [sg.Listbox(values=[f"Nome: {aluno['nome']}, Média: {aluno['media']}, Aproveitamento: {aluno['aproveitamento']}, Situação: {aluno['situação']}" for aluno in alunos], size=(60, 10), key='-ALUNOS-')],
                [sg.Button('sair'), sg.Button('Melhor Aluno')]    

    ]
                
    
    window = sg.Window('Alunos', layout)

    
    while True:
        event, values = window.read()

       
        if event == sg.WIN_CLOSED or event == 'sair':
            window.close()
            nota()
            break
        

        if event == 'Melhor Aluno':
            for aluno in alunos:
                if aluno['media'] > melhor_nota:
                    melhor_nota = aluno['media']
                    melhor_aluno = aluno
                    
            if melhor_aluno:
                sg.popup(f"Melhor aluno: {melhor_aluno['nome']}, media:{melhor_aluno['media']}, aproveitamento {melhor_aluno['aproveitamento']}, situação: {melhor_aluno['situação']}")
                
                
    window.close()


# ----------------------------------- TELA DE REGISTRO ------------------------------------


def cadastro():

    layout = [  [sg.Button('Registrar'), sg.Button('voltar')],
                [sg.Text("Nome usuario")],
                [sg.InputText(key='NOMEUSUARIO')],
                [sg.Text("Email")],
                [sg.InputText(key= 'EMAIL')],
                [sg.Text("Senha")],
                [sg.InputText(password_char='*', key='SENHA')],
                [sg.Text("Confirmar senha")],
                [sg.InputText(password_char='*', key='CONFIRMAR SENHA')],
                [sg.Button('Entrar')]
                ]

    
    window = sg.Window('Registrar', layout)

    
    while True:
        event, values = window.read()

        
        if event == sg.WIN_CLOSED:
            window.close()
            break

        if event == 'voltar':            
            window.close()
            login()
            
        if event == 'Registrar':

            nome= values['NOMEUSUARIO']
            senha= values['SENHA']


            if values['NOMEUSUARIO'] == "" or values['EMAIL'] == "" or values['SENHA'] == "" or values['CONFIRMAR SENHA'] == "":
                sg.popup('ERRO!, insira os campos obrigatorio.')
                continue

            if values['NOMEUSUARIO'].isdigit() or values['EMAIL'].isdigit() :
                sg.popup('ERRO!, o Email e o nome do usuario devem ser texto.')
                continue
            
            if len(values['NOMEUSUARIO']) <3 or len(values['EMAIL']) <3:
                sg.popup('ERRO!, o Email e o nome do usuario devem ter mais de 3 caracteres.')
                continue 

            if '@' not in values['EMAIL'] and '.' not in values['EMAIL']:
                sg.popup('ERRO!, o Email deve ter pelo menos um "@" ou "."')
                continue

            if values['SENHA'] != values['CONFIRMAR SENHA']:
                sg.popup('ERRO!, as senhas nao concidem.')  
                continue 

            if len(values['SENHA']) < 5:
                sg.popup('ERRO!, a senha deve ter pelo menos 5 caracteres.')
                continue  


            with open ('dados_cadastro.txt', 'a') as file:
                file.write(f"{nome}, {senha}\n")
            
            sg.popup('Cadastro realizado com sucesso!')
            window.close()
            login()


    window.close()



# ---------------------------------- TELA DE LOGIN ------------------------------------
def login():

    
    layout = [  [sg.Button('Registrar')],
                [sg.Text("Usuario")],
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
                            sg.popup('Login registrado com sucesso')
                            window.close()
                            nota()
                            break
                           
            else:
                sg.popup('O arquivo não existe')

    window.close()
login()