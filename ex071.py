sacarValor = int(input('Digite um valor: '))

restonotas = 0

notas1 = notas5 = notas10 = notas20 = notas50 = 0

while True:
    
    # Notas 50
    restonotas = sacarValor%50
    notas50 = sacarValor//50

    # Notas 20
    if restonotas >= 20:
        notas20 = restonotas//20
        restonotas = restonotas%20

    # Notas 10
    if restonotas >= 10:
        notas10 = restonotas//10
        restonotas = restonotas%10

    # Notas 5
    if restonotas >= 5:
        notas5 = restonotas//5
        restonotas = restonotas%5

    #Notas 1
    if restonotas >= 1:
        notas1 = restonotas//1

    break

print(f'-------------------------- CAIXA ELETRÔNICO --------------------------\nO valor a ser sacado é: R$ {sacarValor},00\n\nVocê receberá: \n\n{notas50} nota(s) de 50 reais\n{notas20} nota(s) de 20 reais\n{notas10} nota(s) de 10 reais\n{notas5} nota(s) de 5 reais\n{notas1} nota(s) de 1 real\n-------------------------- CAIXA ELETRÔNICO --------------------------')