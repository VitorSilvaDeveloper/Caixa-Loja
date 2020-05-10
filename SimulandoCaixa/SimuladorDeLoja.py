def tabela_preco():

    print('''Forma de pagamento?
    [1] À vista no dinheiro com 10 % de desconto:
    [2] À vista no cartão com 5% de deconto:
    [3] Em até 2x no cartão sem juros:
    [4] Em 3x ou mais no cartão com 20% de juros:
    '''
    )


def avista():
    novo_valor = valor_compra -(valor_compra *10/100)
    print(f'O valor da sua compra que era de R${valor_compra:.2f} agora com desconto é de R${novo_valor:.2f}')


def avista_cartao():
    novo_valor = valor_compra - (valor_compra * 5/100)
    print(f'O valor da sua compra que era de R${valor_compra:.2f} agora com desconto é de R${novo_valor:.2f}')


def cartao_Sjuros():
    novo_valor = valor_compra / 2
    print(f'O valor da sua compra foi de R${valor_compra:.2f} e foi divido em 2x de {novo_valor:.2f}')
    return novo_valor


def cartao_Cjuros():
    novo_valor = valor_compra + (valor_compra * 20 / 100)
    vezes = int(input('Em quantas vezes as compras?'))
    resultado = novo_valor / vezes
    print(f'O valor da sua compra foi de R${valor_compra:.2f} e o novo valor com juros é de R${novo_valor:.2f} divido {vezes}x com parcelas de R${resultado:.2f}')
        
while True:
    valor_compra = float(input('Qual o valor da compra? R$'))
    tabela_preco()

    opcao = int(input('Qual opção?'))

    if opcao == 1:
        avista()
        print('Obrigado e volte sempre!')
    elif opcao == 2:
        avista_cartao()
        print('Obrigado e volte sempre!')

    elif opcao == 3:
        cartao_Sjuros()
        print('Obrigado e volte sempre!')

    elif opcao == 4:
        cartao_Cjuros()
        print('Obrigado e volte sempre!')

    else:
        print('OPÇÃO INVALIDA DE PAGAMENTO, TENTE NOVAMENTE!')

    
