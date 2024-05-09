# 045 Crie um programa que faça o computador jogar Jokenpô com você.

# armazenar opções, apresentar opções e pedir para o usuario escolher uma opção
jogadas = ['pedra', 'papel', 'tesoura']
from random import choice
computador = choice(jogadas)
print('''Vamos jogar Jokenpê, estas são as opções de jogada:
[1] pedra
[2] papel
[3] tesoura''')
opcoes = {1: 'pedra', 2: 'papel', 3: 'tesoura'}
usuario = int(input('Escolha uma opção: '))

print('=>' * 20)
# desconsiderar opções inválidas
if usuario != 1 and usuario != 2 and usuario != 3:
  print('Opção inválida.')
#agora vamos jogar
if computador == 'pedra' and usuario == 2:
  print(f'Você ganhou! Papel ganha de pedra.')
elif computador == 'papel' and usuario == 1:
  print(f'Você perdeu! Papel ganha de pedra.')
elif computador == 'tesoura' and usuario == 1:
  print(f'Você ganhou! Pedra ganha de tesoura.')
elif computador == 'pedra' and usuario == 3:
  print(f'Você perdeu! Pedra ganha de tesoura.')
elif computador == 'papel' and usuario == 3:
  print(f'Você ganhou! Tesoura ganha de papel.')
elif computador == 'tesoura' and usuario == 2:
  print(f'Você perdeu! Tesoura ganha de papel.')
else:
  print('Empate')
print('=>' * 20)
print(f'Computador jogou opção {computador}.')
print(f'Você jogou opção {opcoes[usuario]}.') # isso mostra a escolha do usuario no DICIONARIO/LISTA 'opções'
