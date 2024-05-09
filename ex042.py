# 042 Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
'''- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes'''

ladoA = int(input('Informe a reta A: '))
ladoB = int(input('Informe a reta B: '))
ladoC = int(input('Informe a reta C: '))

if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoA + ladoB:
  print(f'As retas {ladoA}, {ladoB} e {ladoC} podem formar um triângulo.')
  if ladoA == ladoB == ladoC:
    print('É um triângulo equilátero.')
  elif ladoA == ladoB != ladoC or ladoB == ladoA != ladoC or ladoC == ladoA != ladoB:
    print('É um triângulo isósceles.')
  else:
    print('É um triângulo escaleno.')
else:
  print(f'As retas {ladoA}, {ladoB} e {ladoC} não podem formar um triângulo.')
