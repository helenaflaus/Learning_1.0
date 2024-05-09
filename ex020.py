# 020 O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

# este módulo aparentemente sorteia quantos quisermos e depois mostra lista
from random import sample
alunos = ['Bia', 'Helena', 'Paulo', 'Danilo']

sorteio = sample(alunos,4)
print(f'A ordem dos alunos para apresentar é: {sorteio}.')