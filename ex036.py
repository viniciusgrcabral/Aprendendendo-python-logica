valorCasa = float(input('Digite o valor da casa em R$: '))

salario = float(input('Digite o seu salario em R$: '))

anosPagando = int(input('Digite por quantos anos você quer pagar a casa: '))

pagamentoMensalCasa = valorCasa/(anosPagando*12)


if pagamentoMensalCasa > salario * 0.30:
    print('Desculpe, você não pode financiar essa casa por esse tempo')
else:
    print('Você pagará {:.2f} reais durante {} meses'.format(pagamentoMensalCasa, anosPagando*12))