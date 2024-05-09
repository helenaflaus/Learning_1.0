# 015 Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos kms foram percorridos pelo carro? '))
dias = int(input('Por quantos dias ele foi alugado? '))

preço = (dias * 60) + (km * 0.15)

print(f'O custo do aluguel do carro será R$ {preço:.2f}.')
