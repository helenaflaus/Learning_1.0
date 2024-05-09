# 052 Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Descubra se o número é primo: '))
if n == 1:
  print(f'{n} não é primo')
elif n == 2 or n == 3 or n == 5 or n == 7:
  print(f'{n} é primo')
else:
    if n % 2 == 0 or n % 3 == 0 or n % 4 == 0 or n % 5 == 0 or n % 7 == 0:
      print(f'{n} não é primo')
    else:
      print(f'{n} é primo')
