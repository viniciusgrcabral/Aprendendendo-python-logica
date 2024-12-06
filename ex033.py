n1, n2, n3 = input('Digite os numeros separados por espaço: ').split()

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

if n2 < n1 > n3:
    print ('numero maior %d' % n1)
elif n1 < n2 > n3:
   print ('numero maior %d' % n2)
else:
    print ('numero maior %d' % n3)
    
    
if n2 > n1 < n3:
    print ('numero menor %d' % n1)
elif n1 > n2 < n3:
    print ('numero menor %d' % n2)
else:
    print ('numero menor %d' % n3)