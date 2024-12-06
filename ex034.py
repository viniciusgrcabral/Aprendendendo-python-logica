salario = int(input( 'Digite o seu salário: '))

aumento = salario*0.10

aumento2 = salario*0.15

if salario > 1250:
    novo_salario = salario + aumento
    print('Seu novo salario é: %g reais' % novo_salario)
else:
    novo_salario = salario + aumento2
    print('Seu novo salario é: %g reais' % novo_salario)
    