n = 0

for i in range (1, 501):
    if i % 2 != 0 and i % 3 == 0:
        n += i

print (n)

# Outra opção para pôr apenas 1 condição no if é deixar:
# for i in range (1, 501, 2)
# Dessa forma o for vai percorrer apenas os números ímpares