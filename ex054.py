from datetime import date

data_atual = date.today()

atingiu = 0

nãoAtingiu = 0


for i in range(7):
    
    anoNascimento = int(input('Digite o ano que você nasceu: '))

    calculoIdade = data_atual.year - anoNascimento

    if calculoIdade >= 21:
        atingiu += 1
    else:
        nãoAtingiu += 1
        
  

print('{} pessoas atingiram a maioridade e {} não atingiram'.format(atingiu, nãoAtingiu))