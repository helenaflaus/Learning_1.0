# 031 Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = int(input('Me fale a distância da viagem em km: '))

if km <= 200:
  passagem1 = km * 0.5
  print(f'A passagem vai custar R$ {passagem1:.2f}')
else:
  passagem2 = km * 0.45
  print(f'A passagem vai custar R$ {passagem2:.2f}.')
