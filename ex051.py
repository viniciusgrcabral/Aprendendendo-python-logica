numero = int(input('Digite o primeiro termo da P.A.: '))

razão = int(input('Digite a razão da P.A.: '))

print(numero)

for i in range(9):
    PA = numero + razão
    numero = PA
    print (PA)

# Outra solução, melhor:
# 
# numero = int(input('Digite o primeiro termo da P.A.: '))
#
# razão = int(input('Digite a razão da P.A.: '))
#
# décimoTermo = numero + (10 - 1) * razão
#
# for i in range(numero, décimo, razão)
#   print.....  