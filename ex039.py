import datetime



def idade (anoAtual, anoNascimento):

    Idade = anoAtual - anoNascimento

    return Idade


data = datetime.date.today()

anoAtual = data.year

anoNascimento = int(input('Digite o ano do seu nascimento: '))

idadeAtual = idade(anoAtual, anoNascimento)


if __name__ == '__main__':
   

    if idadeAtual < 18:
        print('Você ainda vai se alistar e falta aproximadamente {} ano(s).'.format(18 - idadeAtual))
    elif idadeAtual == 18:
        print('Chegou a horade se alistar!')
    else:
        print('Já devia ter se alistado há {} ano(s)'.format(idadeAtual - 18))

