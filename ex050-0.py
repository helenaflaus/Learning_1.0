# 050 Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

# usando 6 variáveis e checando se são números pares com if else apenas, sem loop
n1 = int(input('Digite um número inteiro: '))
if n1 % 2 == 0:
  n1 = n1
else:
  n1 = 0
n2 = int(input('Digite um número inteiro: '))
if n2 % 2 == 0:
  n2 = n2
else:
  n2 = 0
n3 = int(input('Digite um número inteiro: '))
if n3 % 2 == 0:
  n3 = n3
else:
  n3 = 0
n4 = int(input('Digite um número inteiro: '))
if n4 % 2 == 0:
  n4 = n4
else:
  n4 = 0
n5 = int(input('Digite um número inteiro: '))
if n5 % 2 == 0:
  n5 = n5
else:
  n5 = 0
n6 = int(input('Digite um número inteiro: '))
if n6 % 2 == 0:
  n6 = n6
else:
  n6 = 0

# agora somando os que restaram e mostrando o resultado solicitado
soma = n1 + n2 + n3 + n4 + n5 + n6
print(f'A soma dos valores pares é {soma:.2f}')
