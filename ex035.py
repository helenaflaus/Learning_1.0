# 035 Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''Para que os três segmentos formem um triângulo, existe o que conhecemos como condição de existência, que é a seguinte:
a soma de dois lados é sempre menor que o terceiro lado.'''

ladoA = int(input('Informe a reta A: '))
ladoB = int(input('Informe a reta B: '))
ladoC = int(input('Informe a reta C: '))

if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoA + ladoB:
  print(f'As retas {ladoA}, {ladoB} e {ladoC} podem formar um triângulo.')
else:
  print(f'As retas {ladoA}, {ladoB} e {ladoC} não podem formar um triângulo.')
