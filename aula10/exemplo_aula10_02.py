
# for i in range (5):
#     total_produzido=float(input('Valor total da venda: '))
#     funcionarios=int(input('Total de Funcionários: '))

#     media_por_func= total_produzido / funcionarios
#     print(f'Média por funcionários = {media_por_func: .2f}')



# For com try - Não para de execurar ,se lança com erro.
for i in range(5):
    try:
        
        total_produzido=float(input('Valor total da venda: '))
        funcionarios=int(input('Total de Funcionários: '))

        media_por_func= total_produzido / funcionarios
        print(f'Média por funcionários = {media_por_func: .2f}')
    except ValueError:
        print('Informe um número.')
    except ZeroDivisionError:
        print('Nenhum funcionário informado.')
    
