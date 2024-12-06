import math

n = float(input('Digite um número real: '))



partes = math.modf(n)

print('A porção inteira de {} é {}'.format(n, partes[1]))

# outras formas de resolver:
#  - método int(n)
#  - método math.trunc(n)
