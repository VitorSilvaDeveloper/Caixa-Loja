from time import sleep

print('='*20+'LOJA SORRISO'+'='*20)

valor_compra = float(input('Qual o valor da compra? R$'))
print('''Forma de pagamento?
[1] À vista no dinheiro com 10 % de desconto:
[2] À vista no cartão com 5% de deconto:
[3] Em até 2x no cartão sem juros:
[4] Em 3x ou mais no cartão com 20% de juros:''')

opcao = int(input('Qual opção?'))
sleep(0.5)

print('Verificando...')
sleep(1)
print('Validando verificação...')
sleep(1)

if opcao == 1:
    novo_valor = valor_compra - (valor_compra * 10/100)
    print('O valor da sua compra que era de R${:.2f} agora com desconto é de R${:.2f}'.format(valor_compra, novo_valor))

elif opcao == 2:
    novo_valor = valor_compra - (valor_compra * 5/100)
    print('O valor da sua compra que era de R${:.2f} agora com desconto é de R${:.2f}'.format(valor_compra, novo_valor))

elif opcao == 3:
    novo_valor = valor_compra / 2
    print('O valor da sua compra foi de R${:.2f} e foi divido em 2x de {:.2f}'.format(valor_compra, novo_valor))

elif opcao == 4:
    novo_valor = valor_compra + (valor_compra * 20 / 100)
    vezes = int(input('Em quantas vezes as compras?'))
    resultado = novo_valor / vezes
    print('O valor da sua compra foi de R${:.2f} e o novo valor com juros é de R${:.2f} divido {}x com parcelas de R${:.2f}'.format(valor_compra, novo_valor, vezes, resultado))

else:
    print('OPÇÃO INVALIDA DE PAGAMENTO, TENTE NOVAMENTE!')

print('Obrigado e volte sempre!')
