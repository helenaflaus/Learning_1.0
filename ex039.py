# 039 Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime

nasceu = int(input('Informe seu ano de nascimento: '))
alistarEm = nasceu + 18
anoHj = datetime.date.today().year

if alistarEm < anoHj:
  if anoHj - nasceu == 19:
    print(f'Vá se alistar! Você já passou 1 ano do seu prazo.')
  else:
    print(f'Vá se alistar! Você já passou {anoHj - alistarEm:.0f} anos do seu prazo.')
elif alistarEm == anoHj:
  print('Está na hora de se alistar.')
else:
  if nasceu + 1 == anoHj:
    print(f'Você ainda não precisa se alistar. Aguarde 1 ano.')
  else:
    print(f'Você ainda não precisa se alistar. Aguarde xxx.')