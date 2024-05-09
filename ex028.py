# 028 Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
# escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

# importar módulo de sorteio
from random import choice
n = [0, 1, 2, 3, 4, 5]
# input() para conferir se o programa está certo rsrs
n = choice(n)

# pedir um número de 0 a 5 para o usuário
usuario = int(input(f'Me fale um número inteiro de 0 a 5: '))

# criar condição para comparar resultado do sorteio e escolha do usuário
if usuario == n:
  print(f'Você acertou, o número sorteado foi {n} e você escolheu {usuario}!')
else:
  print(f'Você errou! O número sorteado foi {n} e você escolheu {usuario}.')
