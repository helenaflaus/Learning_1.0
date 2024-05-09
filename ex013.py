# 013 Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Informe o seu salário atual: '))
salario *= 1.15 # este *= faz a seguinte operação 'salario = salario * 1.15'

print(f'Seu salário com o aumento de 15% será R$ {salario:.2f}.')
