import random

a1 = input('Digite o nome do aluno 1: ')

a2 = input('Digite o nome do aluno 2: ')

a3 = input('Digite o nome do aluno 3: ')

a4 = input('Digite o nome do aluno 4: ')

lista_de_alunos = [a1, a2, a3, a4]
random.shuffle(lista_de_alunos)
               

print('A ordem será: {}'.format(lista_de_alunos))