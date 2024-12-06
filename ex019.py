import random
import emoji

a1 = input('Digite o número do primeiro aluno: ')

a2 =input('Digite o número do segundo aluno: ')

a3 = input('Digite o nome do terceiro aluno: ')

a4 = input('Digite o número do quarto aluno: ')

lista_alunos = [a1, a2, a3, a4]

print(emoji.emojize('O aluno sorteado foi {}! :rolling_on_the_floor_laughing:').format(random.choice(lista_alunos)))
