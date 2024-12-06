frase = str(input('Digite uma frase qualquer para saber se é um palíndromo: ')).strip().upper()

fraseSemEspaço = (frase.replace(' ', ''))

fraseInversa = fraseSemEspaço[::-1]

if fraseSemEspaço == fraseInversa:
    print('É palíndromo!')
else:
    print('Não é palíndromo!')