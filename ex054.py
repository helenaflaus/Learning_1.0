# 054 Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime
ano_hoje = datetime.date.today().year
print(f'ano hoje: {ano_hoje}')

nascimento = [1992, 1991, 2009, 2011, 1987, 1997, 1999] # quis encurtar poderia pedir pro usuario informar também e ai iria adicionando em uma lista vazia
maiores = 0
for i in range(len(nascimento)):
    if nascimento[i] <= (ano_hoje-18):
        maiores += 1
print(f'quantos são maiores: {maiores}')