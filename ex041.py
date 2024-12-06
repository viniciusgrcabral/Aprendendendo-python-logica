import datetime
from ex039 import idadeAtual

if idadeAtual <= 9:
    print('MIRIM')
elif 9 < idadeAtual <= 14:
    print('INFANTIL')
elif 14 < idadeAtual <= 19:
    print('JUNIOR')
elif 19 < idadeAtual <= 20:
    print('SÊNIOR')
else:
    print('MASTER')