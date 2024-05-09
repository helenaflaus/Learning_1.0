# 016 Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''import math
real = float(input('Me informe um número real: '))
print(f'O número {real} tem a parte inteira {math.trunc(real)}.')'''

'''ou'''

'''from math import trunc
real = float(input('Me informe um número real: '))
print(f'O número {real} tem a parte inteira {trunc(real)}.')'''

'''ou'''

real = float(input('Me informe um número real: '))
print(f'O numero {real} tem a parte inteira {int(real)}.')
