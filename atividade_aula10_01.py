#  Atividade - caixa eletrônico - 



print ('=== CAIXA ELETRÔNICO ===\n')
print ('\nBem vindo João!')

print ('\nSaldo em conta : \n R$ 1000.00\n')

try:
    saldo=1000
    saque=float(input('Digite o valor a sacar: '))
    # saldo_final= saldo - saque 
 
except Exception as e:
    print(f'Ops! Verifique os valores digitados! Erro [{e}] ')


else:
    if   saque > saldo:
        print('Saldo insuficiente.\nVerifique o saldo e tente novamente!')
    elif saque <=0:
        print('Digite um valor maior ou igual a 0.')
    else:      
        saldo_final= saldo - saque  
        print (f'\nValor debitado = {saque}\nSaldo em conta = {saldo_final: .2f}\n')    
finally:
    print ('*******Transação finalizada com sucesso.*******')

