reta1, reta2, reta3 = input('Digite o tamanho das 3 retas separados por espaço: '). split()

reta1, reta2, reta3 = float(reta1), float(reta2), float(reta3)

Triangulo =  False

if reta3 + reta2 > reta1 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1:
    Triangulo = True
else:
    Triangulo = False

somaLados = reta1 + reta2 + reta3

if Triangulo == True:
    if reta1 == reta2 and reta2 == reta3:
        print('O triângulo é equilátero')
    elif reta1 != reta2 and reta2 != reta3 and reta1 != reta3:
        print('O triângulo é escaleno')
    else:
        print(' O triângulo é isosceles')
