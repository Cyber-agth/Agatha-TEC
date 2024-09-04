# Inicializando as variáveis
media = 0
melhor_aluno = ''
melhor_nota = 0
lista = []

def rep():
    global melhor_nota, melhor_aluno

    # VERIFICANDO SE A ENTRADA É UM NÚMERO
    while True:
        nome = input('Digite o nome do aluno: ')

        if not nome.isdigit():
            break
        else:
            print('O nome que você digitou é um número. Tente novamente!')


    # VALIDAÇÃO PARA NOTAS
    while True:
        nota1 = input('Digite a primeira nota: ')
        nota2 = input('Digite a segunda nota: ')

        if nota1.isdigit() and nota2.isdigit():
            nota1 = int(nota1)
            nota2 = int(nota2)

            if nota1 > 10 or nota2 > 10:
                print('O sisrema não aceita notas maiores que 10!')

            else:
                media = (nota1 + nota2) / 2
                break
        else:
            print('A nota que você digitou é um texto. Tente novamente!')




    # DETERMINANDO O APROVEITAMENTO
    if media == 10:
        aproveitamento = 'A - Excelente'
    elif media >= 8.0:
        aproveitamento = 'B - Aprovado'
    elif media >= 7.0:
        aproveitamento = 'C - Aprovado'
    elif media >= 6.0:
        aproveitamento = 'D - Aprovado'
    elif media >= 5.0:
        aproveitamento = 'E - Aprovado'
    else:
        aproveitamento = 'F - Reprovado'



    # Verifica se este aluno tem a melhor nota
    if media > melhor_nota:
        melhor_nota = media
        melhor_aluno = nome
        nota = {'melhor_aluno': nome, 'aproveitamento': aproveitamento}

    lista.append({'nome': nome, 'media': media, 'aproveitamento': aproveitamento})



# Função principal de repetição
rep()
while True:
    continuar = input('Deseja continuar? (sim ou não): ')
    if continuar.lower() not in ['sim', 'não']:
        print('O que você digitou é diferente de "sim" ou "não". Tente novamente!')
    elif continuar.lower() == 'sim':
        rep()
    elif continuar.lower() == 'não':
        break



# Printando resultados
print('\n--- Resultados ---')
for i in lista:
    print(f"Aluno: {i['nome']}, media: {i['media']}, aproveitamento: {i['aproveitamento']}")

# Printando o melhor aluno
print(f"\nMelhor Aluno: {melhor_aluno}, aproveitamento: {melhor_nota}")
 