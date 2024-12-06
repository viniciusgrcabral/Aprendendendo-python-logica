
número = int(input('Digite um número: '))


maior = número

menor = número


soma = número

contador = 1

continuar = str(input('Quer continuar [S/N]? ')).upper()  


while continuar == 'S':
    
    número = int(input('Digite um número: '))
    
    contador += 1
    
    soma += número

    média = soma/contador

    if número > maior:
        maior = número
    elif número < menor:
        menor = número

    continuar = str(input('Quer continuar [S/N]? ')).upper()

print(soma)
    
print('A média é {}'.format(float(média)))

print('O maior é {} e o menor é {}'.format(maior, menor))