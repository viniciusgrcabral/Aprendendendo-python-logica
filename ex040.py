nota1 = float(input('Digite sua primeira nota: '))

nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('Reprovado!')
elif 5.0 < media < 6.9:
    print('Recuperação!')
else:
    print('Aprovado!')