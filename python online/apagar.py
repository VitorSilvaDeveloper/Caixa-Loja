# Exercício 02 de Porcentagem em Python
'''A loja percebeu que não quer dar 20% em tudo.
Quer dar 20% em algumas coisas, 10% em outra,
nada em outro produto e até 30% em alguns outros produtos.'''
original = float (input('Qual é o preço do produto? '))
if (original < 5):
# print ('Queremos muito dar um desconto para você: Descontos a partir de R$ 5,00!')
print ('Valor sem desconto: R$ {}'.format(original))
elif (original > 5) and (original < 19.99) :
print ('O produto era: R$', original)
print ('Você ganhou R$ {:.2f} de desconto, parabéns!'.format(original*0.1))
print ('O produto sairá por apenas R$ {:.1f}!'.format(original*0.9))
elif (original > 20) and (original < 39.99) :
print ('O produto era: R$', original)
print ('Você ganhou R$ {:.2f} de desconto, parabéns!'.format(original*0.2))
print ('O produto sairá por apenas R$ {:.1f}!'.format(original*0.8))
elif (original > 40) :
print ('O produto era: R$', original)
print ('Você ganhou R$ {:.2f} de desconto, parabéns!'.format(original*0.3))
print ('O produto sairá por apenas R$ {:.1f}!'.format(original*0.7))

# ******E2 COM O LOJISTA CONCEDENDO A QUANTIDADE DE DESCONTO******
original = float (input('Qual é o preço do produto? '))
desconto = float ( input('Digite o desconto: '))
desconto = desconto / 100
print ('O produto era: R$', original)
print ('Você ganhou R$ {:.2f} de desconto, parabéns!'.format(original*desconto))
print ('O produto sairá por apenas R$ {:.1f}!'.format(original-original*desconto))
