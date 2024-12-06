preco = int(input('Digite o valor normal do produto: '))

formaPagamento = int(input('Digite a forma de pagamento (dinheiro = 1, cheque = 1, débito = 2,  crédito em 2x = 3, 3x ou mais no crédito = outro valor)'))

if formaPagamento == 1:
    preco = preco * 0.90
    print(preco)
elif formaPagamento == 2:
    preco = preco * 0.95
    print(preco)
elif formaPagamento == 3:
    print(preco)
else:
    preco = preco + (preco * 0.20 * formaPagamento)
    print(preco)