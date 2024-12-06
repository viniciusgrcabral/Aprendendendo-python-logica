velocidade_do_carro = int(input('Escreva qual era a velocidade do carro, em quilômetros, no momento: '))

multa = (velocidade_do_carro - 80)*7

multa_pro_format = str(multa)

if velocidade_do_carro > 80:
    print ("Você foi multado em: %d reais" % multa)