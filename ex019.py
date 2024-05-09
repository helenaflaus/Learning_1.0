# 019 Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

# este módulo serve para sortear itens aleatórios
from random import choice
alunos = ['Bia', 'Helena', 'Paulo', 'Danilo']

sorteio = choice(alunos) # esta é um dos módulos que podemos usar para sortear

print(f'O(a) aluno(a) sorteado(a) foi {sorteio}.')
