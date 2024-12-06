from math import pow, sqrt

c1 = float(input('Digite um número para o cateto oposto a hipotenusa: '))

c2 = float(input('Digite um número para o cateto adjascente: '))

hipotenusa = pow(c1, 2) + pow(c2, 2)

print('O resultado da hipotenus entre os catetos {:.2f} e {:.2f} é de {}'.format(c1, c2, sqrt(hipotenusa)))


# Outra maneira seria usando math.hypot(c1, c2)