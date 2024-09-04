import PySimpleGUI as sg


def finalizar(alunos):
    melhor_aluno= 0
    melhor_nota= 0

    #RESUMO ALUNOS
    layout = [  [sg.Text('Lista de alunos')],
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
                sg.popup(f"Melhor aluno: {melhor_aluno['nome']}, media:{melhor_aluno['media']}, aproveitamento {melhor_aluno['aproveitamento']}, situação: {melhor_aluno['situação']}")
                
                
                

        

    window.close()

def nota():
    alunos= []
    

    

    # All the stuff inside your window.
    layout = [  [sg.Text("Nome do aluno:")],
                [sg.InputText(key= 'nome')],
                [sg.Text("Primeria nota:")],
                [sg.InputText(key= 'nota1')],
                [sg.Text('segunda nota:')],
                [sg.InputText(key= 'nota2')],
                [sg.Text('media: ', size= (30, 1)), sg.Text('',key= 'media')],
                [sg.Text('aproveitamento: ', size= (30, 1)), sg.Text('', key= 'aproveitamento')],
                [sg.Text('situação: ', size=(30,1)), sg.Text('',key='situação')],
                [sg.Button('calcular'), sg.Button('Cancel'), sg.Button('finalizar')] 
                
                ]

                
    # Create the Window
    window = sg.Window('Hello Example', layout)

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
                finalizar(alunos)



    #VALIDANDO OS INPUTS
        if event == 'calcular':
            nome = values['nome']
            nota1= values['nota1']
            nota2= values['nota2']


            if nome.isdigit():
                sg.popup('ERRO!, o nome deve ser texto.')
               
            
            elif len(nome) <3:
                sg.popup('ERRO!, o nome tem menos de 3 caracteres.')
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
                        elif media >= 7.9 and media >= 7.0:
                            aproveitamento = 'C'
                        elif media >= 6.9 and media >= 6.0:
                            aproveitamento = 'D'
                        elif media >= 5.9 and media >= 5.0:
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
nota()