número = int(input())

razão = int(input())

contador = 0

print(número)

while contador <= 10:
    PA = número + razão
    número = PA
    contador += 1
    print(PA)