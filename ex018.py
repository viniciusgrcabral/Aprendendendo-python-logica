import math

angulo = float(input('Digite um ângulo desejado: '))

radianos = math.radians(angulo)

seno = math.sin(radianos)

cosseno = math.cos(radianos)

tangente = math.tan(radianos)

print('O seno, cosseno e tangente do ângulo {:.2f} são, respectivamente: {:.4f}, {:.4f} e {:.4f}'.format(angulo, seno, cosseno, math.ceil(tangente)))