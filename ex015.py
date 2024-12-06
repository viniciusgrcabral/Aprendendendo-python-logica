dias_alugados = int(input('Quantos dias alugados? '))

kms_rodados = float(input('Quantos Km rodados? '))

total_dias = dias_alugados*60

total_kms = kms_rodados*0.15

print('O total a pagar é de {:.2f}'.format(total_dias+total_kms))