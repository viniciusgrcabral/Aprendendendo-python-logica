somaIdade= 0

maisVelho = 0

contadorIdadesMulheres = 0

for i in range (1, 5):
    print('----- {}º PESSOA -----'.format(i))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))

    somaIdade += idade

    if maisVelho < idade:
        maisVelho = idade
    if sexo == 'F' and idade < 20:
        contadorIdadesMulheres += 1

mediaIdade = somaIdade/4


print('A média de idade do grupo é de {} anos\nO homem mais velho tem {} anos e se chama {}\n Ao todo são {} mulheres de 20 anos'.format(mediaIdade, idade, maisVelho, contadorIdadesMulheres,))

