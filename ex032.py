# 032 Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''Se o ano não termina em 00, ele é bissexto caso seja divisível por 4. Exemplos: 1988, 1992, 1996, 2004, e assim por diante.
# Nota: Um ano é bissexto se ele FOR divisível por 4 e se ele NÃO FOR divisível por 100. '''

ano = int(input('Me fale o ano para descobrir se ele é bissexto: '))

if ano % 400 == 0:
  print(f'O ano {ano} é bissexto!')
elif ano % 4 == 0 and ano % 100 != 0:
  print(f'O ano {ano} é bissexto!')
else:
  print(f'O ano {ano} não é bissexto.')
