número = int(input())

razão = int(input())

contador = 0

total = 0

termos = 9

print(número)

    
while termos != 0:
    total = total + termos
    while contador < total:
        PA = número + razão
        número = PA
        contador += 1
        print(PA)
    termos = int(input('Você deseja ver mais quantos termos? '))