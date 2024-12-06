número = int(input('Digite um número: '))


# -- USANDO WHILE -- 

        # fatorial = número

        # while número > 1:
        #     fatorial = fatorial * (número - 1)
        #     número = número - 1

        # print(fatorial)

# -- OU (WHILE) --

        # n = int(input())
        # c = n
        # f = 1

        # while c > 1
        #       f *= f
        #       c -= 1

# -- USANDO FOR --

        # for i in range (número, 1, -1):
        #     fatorial = fatorial * (i - 1)

        # print(fatorial)


# -- USANDO RECURSÃO --

def recursão (número):
    if número == 0 or número == 1:
        return número
    else:
        return número * recursão(número - 1)
    


print(recursão(número))
