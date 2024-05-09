# 008 Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Me dê o valor em metros a ser convertido: '))
centimentros = metros * 100
milimetros = metros * 1000
print(f'A distância {metros:.1f}m equivale a {centimentros:.1f}cm e {milimetros:.1f}mm.')
