#calculo de produtividade
#-------------------------


print('=== Cálculo de Produtividade ===')

try:
    print('\n----------------------------------')
    total_produzido=float(input('Valor total da venda: '))
    funcionarios=int(input('Total de Funcionários: '))
    media_por_func= total_produzido / funcionarios
    print(f'Média por funcionários = {media_por_func: .2f}')
except ValueError:
    print('Informe um número.')
except ZeroDivisionError:
    print('Nenhum funcionário informado.')