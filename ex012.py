# 012 Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Me fale o preço do produto que deseja: '))
desconto = preco*0.95
print(f'O produto com desconto de 5% fica {desconto:.2f}.')