valor_original = float( input('Valor original: R$'))
desconto = float( input('Desconto (em %) para esse produto:'))
desconto = desconto / 100
print ('Valor original:     R$', valor_original)
print ('Desconto ganho:     R$', valor_original * desconto)
print ('Valor com Desconto: R$', valor_original * (1-desconto) )
