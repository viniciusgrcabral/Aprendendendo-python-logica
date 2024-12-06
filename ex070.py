nome = preço = soma = contadorProdutoMaisDe1000 = produtoMaisBarato =0

maisBarato = float('inf')

while True:

    # Entrada dos produtos
    nome = str(input('Digite o nome do produto: ')).upper()
    preço = float(input('Digite o valor dele: '))

    # Soma
    soma += preço

    # Atualizar contador
    if preço > 1000:
        contadorProdutoMaisDe1000 += 1

    # Atualizar produto mais barato
    if preço < maisBarato:
        maisBarato = preço
        produtoMaisBarato = nome

    continuar = str(input('Quer cadastrar mais um produto [S/N]? ')).upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer cadastrar mais um produto [S/N]? ')).upper()
    if continuar == 'N':
        print(f'Soma total R$ {soma:.2f}, {contadorProdutoMaisDe1000} com mais de mil reais de valor e o produto mais barato foi {produtoMaisBarato}')
        break
    