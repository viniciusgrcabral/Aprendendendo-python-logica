idade = contadorIdade = 0

sexo = contadorFemininoMenor20 = contadorMasculino = 0

continuar = 0

while True:

    # Perguntas de dados e validações
    idade = int(input('Digite uma idade: '))
    sexo = str(input('Digite o sexo [F/M]: ')).upper()
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Digite o sexo [F/M]: ')).upper()
    
    # Atualização de contadores
    if idade >= 18:
        contadorIdade += 1
    if sexo == 'M':
        contadorMasculino += 1
    if sexo == 'F' and idade < 20:
        contadorFemininoMenor20 += 1

    # Verificando continuidade    
    continuar = str(input('Quer cadastrar mais alguém [S/N]? ')).upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer cadastrar mais alguém [S/N]? ')).upper()
    if continuar == 'N':
        break

print(f'---------------------------------------------\nExistem {contadorIdade} com mais de 18\nExistem {contadorMasculino} homens cadastrados\nExistem {contadorFemininoMenor20} mulheres com menos de 20 anos\n---------------------------------------------')