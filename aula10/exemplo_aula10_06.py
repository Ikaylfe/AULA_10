def calcular_media(lista_notas):
    tot=sum(lista_notas)
    media= tot / len(lista_notas) # len() lê a qtde de dados dentro da lista no caso da média são 4
    return tot, media


contador= 1

while True:
    print(f'Aluno {contador}')
    aluno = input('Nome do aluno:')

    notas= []
    try:
        for i in range(4):
            nota= float(input('Informe a nota:  '))
            notas.append(nota)
    except ValueError:
        print('Erro:Informe apenas valores válidos!')        
    else:
        total,media = calcular_media(notas)
        
        print('RESULTADO')
        print(f'Aluno: {aluno}')
        print(f'Total de pontos: {total}')
        print(f'Média: {media: .2f}')

    finally:
        print('Processo encerrado!')

  


    opcao= input('Deseja calcular para outro aluno? [s/n]').strip().upper() #.strip() - REMOVE ESPAÇOS .upper() - Letras maiusculas
    if opcao != 'S':
            break
    contador +=1
    print('\nPrograma encerrado.')    