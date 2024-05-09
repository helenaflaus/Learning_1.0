# 007 Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

p1 = float(input('Insira nota P1: '))
p2 = float(input('Insira nota P2: '))
media = (p1 + p2) / 2
if media > 6:
  print(f'Aprovada! Sua média aritmética é {media:.1f}.')
else:
  print(f'Reprovada, nos vemos na P3, sua média é {media:.1f}.')