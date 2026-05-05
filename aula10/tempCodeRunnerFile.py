print('=== Cálculo de Produtividade ===')
try:
    print('----------------------------------\n')
    total_produzido=float(input('Valor total da venda: '))
    funcionarios=int(input('Total de Funcionários: '))
    media_por_func= total_produzido / funcionarios
    
except Exception as e:
    print(f'Ops! Erro nos valores de entrada.\n[{e}]')
except KeyboardInterrupt:
    print('Operação cancelada pelo usuário.')

# se não der erro no código acima executa o "else".
else:
    print(f'Média por funcionários = {media_por_func: .2f}')

#com ou sem erro bloco será executado....
finally:
    print('\nPrograma encerrado!')
