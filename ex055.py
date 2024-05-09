# 055 Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for c in range(0,6):
    peso = float(input('Peso: '))
    if peso > maior:
        maior = peso
    else:
        menor = peso
print(f'maior peso {maior:.2f}')
print(f'menor peso {menor:.2f}')
