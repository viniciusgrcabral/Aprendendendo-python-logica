n = int(input('Digite a quantidade de termos da sequência de fibonacci: '))

contador = 0


sequencia = [0, 1, 1]


while contador < n:

    proximoNúmero = sequencia[-1] + sequencia[-2]
    
    sequencia.append(proximoNúmero)
 
    contador += 1
    
    print (sequencia)