numero = int(input('Digite um número: '))


if numero == 2:
    print('primo')
else:    
    for i in range(2, numero):
        if numero % i != 0:
            print('primo')
        else:
            print('não é primo')
        break


# numero = int(input(...))
# c = 0
# total = 0
# for c in range(1, numero)
#    if numero % c == 0
#       total += 1
# if total == 2
#   print('Primo')
# else:
#   print não é primo