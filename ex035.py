r1, r2, r3 = input('Digite o tamanho das 3 retas separados por espaçõ: ').split()

r1 = int(r1)
r2 = int(r2)
r3 = int(r3)

if r3+r2 > r1 and r2 < r1 + r3 and r1 < r2 +r3:
    print('É possível fazer um triângulo')
    triangulo = True
else:
    print('Não é possivel fazer um triângulo')
    triangulo = False


