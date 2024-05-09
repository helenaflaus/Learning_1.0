# 051 Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

a1 = int(input('Digite o 1º termo: '))
razao = int(input('Digite a razão: '))

print(f'Os 10 primeiros termos da PA de {a1} com razão {razao}: ')

for i in range(1, 11):
  termo_de_i = a1 + (i - 1) * razao
  print(termo_de_i)

print('fim')
