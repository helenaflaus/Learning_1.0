# 014 Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Me informe a temperatura em Celsius: '))
fahrenheit = (celsius * 1.8) + 32
print(f'A temperatura em graus Fahrenheit é {fahrenheit:.2f}.')