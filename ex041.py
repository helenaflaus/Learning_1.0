# 041 A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
'''- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''

idade = int(input('Idade: '))

if idade <= 9:
  print('Mirim.')
elif 9 < idade <= 14:
  print('Infantil.')
elif 14 < idade <= 19:
  print('Júnior.')
elif 19 < idade <= 25:
  print('Sênior.')
else:
  print('Master.')
