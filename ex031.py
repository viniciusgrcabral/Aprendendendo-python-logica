distância = float(input('Digite a distância da viagem em quilômetros: '))

if distância < 200:
    preço_da_viagem_curta = distância * 0.5
    print('Sua viagem custará %g reais' % preço_da_viagem_curta)
else:
    preço_da_viagem_longa = distância * 0.45
    print('Sua viagem custará %g reais' % preço_da_viagem_longa)