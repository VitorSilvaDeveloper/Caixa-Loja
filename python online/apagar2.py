# Valor inicial aplicado
vi = float( input('Valor inicial: ') )

# Rentabilidade mensagem, em %
i = float ( input('Rentabilidade mensal: ') )

# Transformando a porcentagem em valor numérico
i = i / 100

# Tempo de investimento
m = int( input('Meses que vai deixar rendendo: ') )

vf = vi * (1+i)**m

print('Valor apos ',m,' meses: R$ ',vf)
