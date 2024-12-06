numero = int(input('Digite um numero inteiro qualquer: '))

conversor = int(input('Digite qual conversão quer fazer, 1 (Binário), 2 (Octal) e 3 (Hexadecimal):'))

if conversor == 1:
    print(bin(numero)[2:])
elif conversor == 2:
    print(oct(numero)[2:])
elif conversor == 3:
    print(hex(numero)[2:])
else:
    print('Opção inválida, tente novamente')