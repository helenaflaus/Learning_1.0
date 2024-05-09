# 037 Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input('Me dê um número inteiro: '))
print('''Escolha uma das bases de conversão:
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal
''')
conversao = int(input('Sua opção: '))

if conversao == 1:
  print(f'O número {n} convertido para binário é igual a {bin(n)[2:]}.') # existe função 'bin(x)' para converter
elif conversao == 2:
  print(f'O número {n} convertido para octal é igual a {oct(n)[2:]}.') # existe função 'oct(x)' para converter
elif conversao == 3:
  print(f'O número {n} convertido para hexadecimal é igual a {hex(n)[2:]}.') # existe função 'hex(x)' para converter
else:
  print('Opção inválida.')
