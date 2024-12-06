largura = float(input('Digite a largura da parede: '))

altura = float(input('Digite a altura da parede: '))

print('A área da parede é {:.2f}m² e é necessário {:.2f}l de tinta para pintá-la'.format(largura*altura, (largura*altura)/2))